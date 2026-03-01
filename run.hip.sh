#!/bin/bash

# SPDX-FileCopyrightText: Copyright (c) 2022-2025, NVIDIA CORPORATION & AFFILIATES.
# SPDX-FileCopyrightText: Copyright (c) 2026 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: BSD-3-Clause AND MIT

# NOTE: ensure all dir changes are relative to the location of this
# script, and that this script resides in the repo dir!
# shellcheck disable=SC2164
REPODIR=$(cd "$(dirname "$0")"; pwd)

printHelp() {
    echo "Usage: $0 [options] [targets]"

    echo ""
    cat <<EOF
Targets:
    cpp_tests            - run all C++ tests
    cpp_bench            - run C++ benchmarks
    cpp_examples         - run C++ examples
    py_tests             - run all Python core tests
    py_async_tests       - run all Python async tests
    py_bench             - run Python core benchmarks
    py_async_bench       - run Python async benchmarks
    cython_tests         - run all Python tests of public Cython API (implies py_tests)

Options:
    --build-dir         - specify the build directory (default: is the default
                          build directory of build.hip.sh)
    -h | --help         - show this help text

Supported environment variables:
    UCXX_BUILD_DIR      - specify build directory (overridden by --build-dir)
EOF

    echo ""
    echo "default action is to run all of the above targets"
}

# process the flags and arguments
TARGETS=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    --build-dir) BUILD_ROOT="$2"; shift 2 ;;
    --build-dir=*) BUILD_ROOT="${1#*=}"; shift ;;
    -h|--help) printHelp; exit 0 ;;
    -*) echo "Unknown option: $1" >&2; exit 1 ;;
    *) TARGETS+=("$1"); shift ;;
  esac
done

# Check for invalid targets
VALID_TARGETS=(
  "cpp_tests" "cpp_bench" "cpp_examples"
  "py_tests"  "py_async_tests" "py_bench" "py_async_bench" "cython_tests"
)
for t in "${TARGETS[@]}"; do
  if ! (echo " ${VALID_TARGETS[*]} " | grep -q " ${t} "); then
    echo "Invalid target, check --help: ${t}"
    exit 1
  fi
done

hasTarget() {
  for t in "${TARGETS[@]}"; do
    [[ $t == "$1" ]] && return 0
  done
  return 1
}

# handle automatic target enablement
if [[ ${#TARGETS[@]} -eq 0 ]]; then
  TARGETS=("${VALID_TARGETS[@]}")
fi

if hasTarget cython_tests; then
  TARGETS+=("py_tests")
fi

BINARY_PATH=${BUILD_ROOT:-"${REPODIR}"}/cpp/build

SUMMARY_RESULTS=()

#------------------------------------------------------------------------------
# UCX_TCP_CM_REUSEADDR=y to be able to bind immediately to the same port before
export UCX_TCP_CM_REUSEADDR=y

run_cpp_tests() {
  CONFIG_NAME="CPP_TEST"

  echo -e "\e[1mRunning: ${CONFIG_NAME}\e[0m"
  CMD="${BINARY_PATH}/gtests/UCXX_TEST"
  echo "$CMD"; eval "$CMD"
  RET=$?

  SUMMARY_RESULTS+=("${CONFIG_NAME}.........$([ $RET -eq 0 ] && echo Success || echo "Error Code: $RET")")
}

run_cpp_benchmark() {
  PROGRESS_MODE=$1
  TEST_TYPE=$2
  MEMORY_TYPE=$3

  CONFIG_NAME="CPP_Benchmark with PROGRESS_MODE=${PROGRESS_MODE}, TEST_TYPE=${TEST_TYPE}, MEMORY_TYPE=${MEMORY_TYPE}"

  SERVER_PORT=12345
  MESSAGE_SIZE="8388608"
  NUM_ITERATIONS="20"
  NUM_WARMUP="3"
  PERCENTILE_RANK="50.0"

  CMD_BASE="${BINARY_PATH}/benchmarks/ucxx_perftest"
  CMD_OPTS="-t ${TEST_TYPE} -m ${MEMORY_TYPE} -P ${PROGRESS_MODE} -p ${SERVER_PORT} -s ${MESSAGE_SIZE} -n ${NUM_ITERATIONS} -w ${NUM_WARMUP} -R ${PERCENTILE_RANK} -v"
  SERVER_CMD="${CMD_BASE} ${CMD_OPTS}"
  CLIENT_CMD="${CMD_BASE} ${CMD_OPTS} 127.0.0.1"

  echo -e "\e[1mRunning: ${CONFIG_NAME}\e[0m"
  echo "SERVER_CMD: ${SERVER_CMD}"
  echo "CLIENT_CMD: ${CLIENT_CMD}"
  ${SERVER_CMD} &
  pid=$!
  sleep 1
  ${CLIENT_CMD}
  RET1=$?
  wait $pid
  RET2=$?

  SUMMARY_RESULTS+=("${CONFIG_NAME}.........$([[ $RET1 -eq 0 && $RET2 -eq 0 ]] && echo Success || echo "Error Code: $RET1, $RET2")")
}

run_cpp_example() {
  PROGRESS_MODE=$1
  SEND_BUFFER_TYPE=$2
  RECV_BUFFER_TYPE=$3

  CONFIG_NAME="CPP_Example with PROGRESS_MODE=${PROGRESS_MODE}, SEND_BUFFER_TYPE=${SEND_BUFFER_TYPE}, RECV_BUFFER_TYPE=${RECV_BUFFER_TYPE}"

  echo -e "\e[1mRunning: ${CONFIG_NAME}\e[0m"
  CMD="${BINARY_PATH}/examples/ucxx_example_basic -P ${PROGRESS_MODE} -s ${SEND_BUFFER_TYPE} -r ${RECV_BUFFER_TYPE}"
  echo "$CMD"; eval "$CMD"
  RET=$?

  SUMMARY_RESULTS+=("${CONFIG_NAME}.........$([ $RET -eq 0 ] && echo Success || echo "Error Code: $RET")")
}

run_py_tests() {
  ARGS=$1

  CONFIG_NAME="Python_Tests with ARGS=${ARGS}"

  echo -e "\e[1mRunning: ${CONFIG_NAME}\e[0m"
  CMD="pytest -vs --import-mode=append python/ucxx/ucxx/_lib/tests/ ${ARGS}"
  echo "$CMD"; eval "$CMD"
  RET=$?

  SUMMARY_RESULTS+=("${CONFIG_NAME}.........$([ $RET -eq 0 ] && echo Success || echo "Error Code: $RET")")
}

run_py_async_tests() {
  PROGRESS_MODE=$1
  ENABLE_DELAYED_SUBMISSION=$2
  ENABLE_PYTHON_FUTURE=$3
  SKIP=$4

  CONFIG_NAME="Python_Async_Tests with PROGRESS_MODE=${PROGRESS_MODE} ENABLE_DELAYED_SUBMISSION=${ENABLE_DELAYED_SUBMISSION} ENABLE_PYTHON_FUTURE=${ENABLE_PYTHON_FUTURE}"

  if [ "$SKIP" -ne 0 ]; then
    echo -e "\e[31;1mSkipping unstable test: ${CONFIG_NAME}\e[0m"
  else
    echo -e "\e[1mRunning: ${CONFIG_NAME}\e[0m"
    CMD="UCXPY_PROGRESS_MODE=${PROGRESS_MODE} UCXPY_ENABLE_DELAYED_SUBMISSION=${ENABLE_DELAYED_SUBMISSION} UCXPY_ENABLE_PYTHON_FUTURE=${ENABLE_PYTHON_FUTURE} pytest -vs --import-mode=append python/ucxx/ucxx/_lib_async/tests/"
    echo "$CMD"; eval "$CMD"
    RET=$?

    SUMMARY_RESULTS+=("${CONFIG_NAME}.........$([ $RET -eq 0 ] && echo Success || echo "Error Code: $RET")")
  fi
}

run_py_benchmark() {
  BACKEND=$1
  PROGRESS_MODE=$2
  ASYNCIO_WAIT=$3
  ENABLE_DELAYED_SUBMISSION=$4
  ENABLE_PYTHON_FUTURE=$5
  N_BUFFERS=$6
  SLOW=$7

  CONFIG_NAME="Python_Benchmark with BACKEND=${BACKEND}, PROGRESS_MODE=${PROGRESS_MODE}, ASYNCIO_WAIT=${ASYNCIO_WAIT}, ENABLE_DELAYED_SUBMISSION=${ENABLE_DELAYED_SUBMISSION}, ENABLE_PYTHON_FUTURE=${ENABLE_PYTHON_FUTURE}, N_BUFFERS=${N_BUFFERS}, SLOW=${SLOW}"

  ASYNCIO_WAIT=$([ "$ASYNCIO_WAIT" -ne 0 ] && echo "--asyncio-wait" || echo "")

  echo -e "\e[1mRunning: ${CONFIG_NAME}\e[0m"
  if [ "$SLOW" -ne 0 ]; then
    echo -e "\e[31;1mSLOW BENCHMARK: it may seem like a deadlock but will eventually complete.\e[0m"
  fi

  CMD="UCXPY_ENABLE_DELAYED_SUBMISSION=${ENABLE_DELAYED_SUBMISSION} UCXPY_ENABLE_PYTHON_FUTURE=${ENABLE_PYTHON_FUTURE} python -m ucxx.benchmarks.send_recv --backend ${BACKEND} -o cupy --reuse-alloc -d 0 -e 1 -n 8MiB --n-buffers $N_BUFFERS --progress-mode ${PROGRESS_MODE} ${ASYNCIO_WAIT}"
  echo "$CMD"; eval "$CMD"
  RET=$?

  SUMMARY_RESULTS+=("${CONFIG_NAME}.........$([ $RET -eq 0 ] && echo Success || echo "Error Code: $RET")")
}

#------------------------------------------------------------------------------
# Let all tests run even if they fail
set +e

if hasTarget cpp_tests; then
  run_cpp_tests
fi

if hasTarget cpp_bench; then
  # run_cpp_benchmark PROGRESS_MODE
  for test_type in tag_lat tag_bw; do
    for mem_type in host cuda cuda-managed cuda-async; do
      run_cpp_benchmark   polling         ${test_type} ${mem_type}
      run_cpp_benchmark   blocking        ${test_type} ${mem_type}
      run_cpp_benchmark   thread-polling  ${test_type} ${mem_type}
      run_cpp_benchmark   thread-blocking ${test_type} ${mem_type}
      run_cpp_benchmark   wait            ${test_type} ${mem_type}
    done
  done
fi

if hasTarget cpp_examples; then
  for send_buffer_type in host rmm; do
    for recv_buffer_type in host rmm; do
      # run_cpp_example PROGRESS_MODE   SEND_BUFFER_TYPE    RECV_BUFFER_TYPE
      run_cpp_example   polling         ${send_buffer_type} ${recv_buffer_type}
      run_cpp_example   blocking        ${send_buffer_type} ${recv_buffer_type}
      run_cpp_example   thread-polling  ${send_buffer_type} ${recv_buffer_type}
      run_cpp_example   thread-blocking ${send_buffer_type} ${recv_buffer_type}
      run_cpp_example   wait            ${send_buffer_type} ${recv_buffer_type}
    done
  done
fi

if hasTarget py_tests; then
  if hasTarget cython_tests; then
    ARGS="--run-cython"
  else
    ARGS=""
  fi
  run_py_tests ${ARGS}
fi

if hasTarget py_async_tests; then
  # run_py_async_tests PROGRESS_MODE   ENABLE_DELAYED_SUBMISSION ENABLE_PYTHON_FUTURE SKIP
  run_py_async_tests   polling         0                         0                    0
  run_py_async_tests   polling         0                         1                    0
  run_py_async_tests   polling         1                         0                    1    # Delayed submission can't be used with polling
  run_py_async_tests   polling         1                         1                    1    # Delayed submission can't be used with polling
  run_py_async_tests   thread-polling  0                         0                    0
  run_py_async_tests   thread-polling  0                         1                    0
  run_py_async_tests   thread-polling  1                         0                    0
  run_py_async_tests   thread-polling  1                         1                    0
  run_py_async_tests   thread          0                         0                    0
  run_py_async_tests   thread          0                         1                    0
  run_py_async_tests   thread          1                         0                    0
  run_py_async_tests   thread          1                         1                    0
fi

if hasTarget py_bench; then
  # run_py_benchmark  BACKEND   PROGRESS_MODE   ASYNCIO_WAIT  ENABLE_DELAYED_SUBMISSION ENABLE_PYTHON_FUTURE NBUFFERS SLOW
  run_py_benchmark    ucxx-core blocking        0             0                         0                    1        0
  run_py_benchmark    ucxx-core polling         0             0                         0                    1        0
  run_py_benchmark    ucxx-core thread-polling  0             0                         0                    1        0
  run_py_benchmark    ucxx-core thread-polling  1             0                         0                    1        0
  run_py_benchmark    ucxx-core thread          0             0                         0                    1        0
  run_py_benchmark    ucxx-core thread          1             0                         0                    1        0
fi

if hasTarget py_async_bench; then
  for nbuf in 1 8; do
    # run_py_benchmark    BACKEND     PROGRESS_MODE   ASYNCIO_WAIT  ENABLE_DELAYED_SUBMISSION ENABLE_PYTHON_FUTURE NBUFFERS SLOW
    run_py_benchmark      ucxx-async  polling         0             0                         0                    ${nbuf}  0
    run_py_benchmark      ucxx-async  polling         0             0                         1                    ${nbuf}  0
    # Delayed submission can't be used with polling
    #run_py_benchmark     ucxx-async  polling         0             1                         0                    ${nbuf}  0
    #run_py_benchmark     ucxx-async  polling         0             1                         1                    ${nbuf}  0
    run_py_benchmark      ucxx-async  thread-polling  0             0                         0                    ${nbuf}  0
    run_py_benchmark      ucxx-async  thread-polling  0             0                         1                    ${nbuf}  0
    run_py_benchmark      ucxx-async  thread-polling  0             1                         0                    ${nbuf}  0
    run_py_benchmark      ucxx-async  thread-polling  0             1                         1                    ${nbuf}  0
    if [ ${nbuf} -eq 1 ]; then
      run_py_benchmark    ucxx-async  thread          0             0                         0                    ${nbuf}  1
      run_py_benchmark    ucxx-async  thread          0             0                         1                    ${nbuf}  1
      run_py_benchmark    ucxx-async  thread          0             1                         0                    ${nbuf}  1
    else
      run_py_benchmark    ucxx-async  thread          0             0                         0                    ${nbuf}  0
      run_py_benchmark    ucxx-async  thread          0             0                         1                    ${nbuf}  0
      run_py_benchmark    ucxx-async  thread          0             1                         0                    ${nbuf}  0
    fi
    run_py_benchmark      ucxx-async  thread          0             1                         1                    ${nbuf}  0
  done
fi

echo "Results Summary"
echo "--------------------------------------------------------------------------------------------"
for line in "${SUMMARY_RESULTS[@]}"; do
  echo "$line"
done
echo "--------------------------------------------------------------------------------------------"
