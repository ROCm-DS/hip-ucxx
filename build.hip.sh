#!/bin/bash

# SPDX-FileCopyrightText: Copyright (c) 2022-2025, NVIDIA CORPORATION & AFFILIATES.
# SPDX-FileCopyrightText: Copyright (c) 2026 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: BSD-3-Clause AND MIT

# UCXX build script for AMD platform
#------------------------------------

# This script simplifies the build process of the components in this repo by
# choosing the most common build options. Some customization is possible using
# command line arguments (see the help output for details). Use CMake and/or pip
# directly for more customization options

# Abort script on first error
set -e

# NOTE: ensure all dir changes are relative to the location of this
# script, and that this script resides in the repo dir!
# shellcheck disable=SC2164
REPODIR=$(cd "$(dirname "$0")"; pwd)

printHelp() {
    echo "Usage: $0 [options] [targets]"

    echo ""
    cat <<EOF
Core Build Targets:
    clean               - remove all existing build artifacts and configuration
                          (start from a clean state)
    uninstall           - remove all the installed files as per the
                          'install_manifest.txt' file in the libucxx build
                          directory
    all                 - build all targets

C++ targets:
    libucxx             - build the libucxx C++ library
    libucxx-tests       - build the libucxx C++ tests (implies 'libucxx')
    libucxx-ex          - build the libucxx C++ examples (implies 'libucxx')
    libucxx-bench       - build the libucxx C++ benchmarks (implies 'libucxx')
    libucxx-py-api      - build the libucxx Python bindings support module
                          (implies libucxx, automatically enabled when 'ucxx',
                          'libucxx', and '--find-libucxx' are all enabled)
    cxx-all             - build all C++ targets

Python targets:
    libucxx_py          - build the Python module that loads the libucxx
                          shared library (enabled when 'ucxx' is used without
                          '--find-libucxx')
    ucxx                - build the ucxx Python module
    ucxx-cython-tests   - build the ucxx Cython tests (implies 'ucxx')
    distributed_ucxx    - build the ucxx backend for dask/distributed
    py-all              - build all Python targets

Build options:
    --build-dir         - specify a build directory (useful for out-of-source
                          builds; default is in-source)
    --install-prefix    - specify an install prefix for the libucxx C++ module
    --find-libucxx      - use an existing libucxx build/installation for the
                          ucxx build. The python binding module is also
                          expected to be available. Also searches in the C++
                          build or install directory.
    --gpu-archs         - GPU architectures to target (options: rapids,
                          native (default), or a comma-separated list)
    -j                  - specify number of jobs for parallel builds
    -v                  - enable verbose build output
    -g                  - build with debug settings
    -n                  - skip install step (builds wheels for Python modules)
    -c                  - generate compile_commands.json

Help:
    -h | --help         - show this help text
EOF

    echo ""
    cat << EOF
To reduce verbosity and/or maintain consistency across invocations, certain environment variables can be set.
NOTE: Corresponding command line options will override these.

    UCXX_BUILD_DIR         - for --build-dir
    UCXX_INSTALL_PREFIX    - for --install-prefix
    UCXX_FIND_LIBUCXX      - for --find-libucxx
    UCXX_BUILD_TYPE        - specify a CMake build type
    UCXX_HIP_ARCHITECTURES - specify the gpu archs (--gpu-archs),
                             overrides RAPIDS_CMAKE_HIP_ARCHITECTURES
EOF

    echo ""
    echo "default action when no targets are specified is to build and install 'ucxx' and 'distributed_ucxx'"
}

#--------------------------------------------------------------------------------------------------
processGpuArchs() {
    local input="$1"
    local upper="${input^^}"   # convert to uppercase

    case "$upper" in
        NATIVE|RAPIDS) printf '%s' "$upper" ;;
        *) printf '%s' "${input//,/;}" ;;
    esac
}

#--------------------------------------------------------------------------------------------------
# Set defaults for vars modified by flags or environment variable
BUILD_COMPILE_COMMANDS=OFF
VERBOSE=0
NO_INSTALL=0

BUILD_ROOT=${UCXX_BUILD_DIR:-}
INSTALL_PREFIX=${UCXX_INSTALL_PREFIX:=${INSTALL_PREFIX:=${PREFIX:=${CONDA_PREFIX}}}}
FIND_LIBUCXX=${UCXX_FIND_LIBUCXX:=0}
BUILD_TYPE=${UCXX_BUILD_TYPE:="Release"}
GPU_ARCHS=${UCXX_HIP_ARCHITECTURES:=${RAPIDS_CMAKE_HIP_ARCHITECTURES:="NATIVE"}}
PARALLEL_LEVEL=${PARALLEL_LEVEL:=$(nproc)}

# process the flags and arguments
TARGETS=()
while [[ $# -gt 0 ]]; do
    case "$1" in
        -v) VERBOSE=1; shift ;;
        -g) BUILD_TYPE="Debug"; shift ;;
        -n) NO_INSTALL=1; shift ;;
        -c) BUILD_COMPILE_COMMANDS=ON; shift ;;
        -j) PARALLEL_LEVEL="$2"; shift 2 ;;
        -j=*) PARALLEL_LEVEL="${1#*=}"; shift ;;
        --build-dir) BUILD_ROOT="$2"; shift 2 ;;
        --build-dir=*) BUILD_ROOT="${1#*=}"; shift ;;
        --install-prefix) INSTALL_PREFIX="$2"; shift 2 ;;
        --install-prefix=*) INSTALL_PREFIX="${1#*=}"; shift ;;
        --find-libucxx) FIND_LIBUCXX=1; shift ;;
        --gpu-archs) GPU_ARCHS="$(processGpuArchs "$2")"; shift 2 ;;
        --gpu-archs=*) GPU_ARCHS="$(processGpuArchs "${1#*=}")"; shift ;;
        -h|--help) printHelp; exit 0 ;;
        -*) echo "Unknown option: $1" >&2; exit 1 ;;
        *) TARGETS+=("$1"); shift ;;
    esac
done

# Check for invalid targets
VALID_TARGETS=(
    "clean" "uninstall"
    "all" "cxx-all" "py-all"
    "libucxx" "libucxx-tests" "libucxx-ex" "libucxx-bench" "libucxx-py-api"
    "libucxx_py" "ucxx" "ucxx-cython-tests" "distributed_ucxx"
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
    TARGETS+=("ucxx" "distributed_ucxx")
fi

if hasTarget "libucxx-*"; then
    TARGETS+=("libucxx")
fi

if hasTarget ucxx-cython-tests; then
    TARGETS+=("ucxx")
fi

if hasTarget ucxx; then
    if (( ! FIND_LIBUCXX )); then
        TARGETS+=("libucxx_py")
    elif hasTarget libucxx; then
        TARGETS+=("libucxx-py-api")
    fi
fi

if hasTarget all || hasTarget cxx-all; then
    TARGETS+=("libucxx" "libucxx-tests" "libucxx-ex" "libucxx-bench" "libucxx-py-api")
fi
if hasTarget all || hasTarget py-all; then
    TARGETS+=("libucxx_py" "ucxx" "ucxx-cython-tests" "distributed_ucxx")
fi

# build directory structure
if [[ -z "$BUILD_ROOT" ]]; then
    LIBUCXX_BUILD_DIR=${REPODIR}/cpp/build
else
    WHEEL_TAG=$(python3 <<EOF
from packaging import tags
sys_tags_iter=iter(p for p in tags.sys_tags() if 'manylinux' not in p.platform and 'musllinux' not in p.platform)
print(next(sys_tags_iter))
EOF
    )

    LIBUCXX_BUILD_DIR=$BUILD_ROOT/cpp/build
    LIBUCXX_PY_BUILD_DIR=$BUILD_ROOT/python/libucxx
    UCXX_BUILD_DIR=$BUILD_ROOT/python/ucxx
    PYTHON_DIST_DIR=${BUILD_ROOT}/python/dist
fi

#------------------------------------------------------------------------------
# Remove duplicate targets (mainly for neat printing below)
UNIQUE_TARGETS_=()
for t in "${VALID_TARGETS[@]}"; do
    if hasTarget "$t" && [[ $t != *all ]]; then
        UNIQUE_TARGETS_+=("${t}")
    fi
done

TARGETS=("${UNIQUE_TARGETS_[@]}")
unset UNIQUE_TARGETS_


#------------------------------------------------------------------------------
cat <<EOF
Building with the following parameters
---------------------------------------
Build root : ${BUILD_ROOT:-"unspecified"}
Install prefix: ${INSTALL_PREFIX:-"default"}
Build type: ${BUILD_TYPE}
GPU architectures: ${GPU_ARCHS}
Find libucxx library: $([[ ${FIND_LIBUCXX} -eq 1 ]] && echo ON || echo OFF)
Build compile_commands.json: $([[ ${BUILD_COMPILE_COMMANDS} -eq 1 ]] && echo ON || echo OFF)
Verbose build: $([[ ${VERBOSE} -eq 1 ]] && echo ON || echo OFF)
Do install step: $([[ ${NO_INSTALL} -eq 0 ]] && echo ON || echo OFF)
Number of build jobs: ${PARALLEL_LEVEL}
Targets to build: ${TARGETS[*]}
EOF

if hasTarget libucxx; then
    echo "libucxx build directory: ${LIBUCXX_BUILD_DIR}"
fi
if hasTarget libucxx_py; then
    echo "libucxx_py build directory: ${LIBUCXX_PY_BUILD_DIR:-default}"
fi
if hasTarget ucxx; then
    echo "ucxx build directory: ${UCXX_BUILD_DIR:-default}"
fi
if [[ -n ${WHEEL_TAG} ]]; then
    echo "wheel_tag : ${WHEEL_TAG}"
fi
if [[ -n ${PYTHON_DIST_DIR} ]]; then
    echo "wheels output folder: ${PYTHON_DIST_DIR}"
fi
echo "------------------------------------------------------------------------"

#------------------------------------------------------------------------------
export RAPIDS_CMAKE_HIP_ARCHITECTURES=${GPU_ARCHS}

#------------------------------------------------------------------------------
if hasTarget clean; then
    set -x
    rm -rf "${LIBUCXX_BUILD_DIR}"
    if [ -n "${LIBUCXX_PY_BUILD_DIR}" ]; then
        rm -rf "${LIBUCXX_PY_BUILD_DIR}"
    fi
    if [ -n "${UCXX_BUILD_DIR}" ]; then
        rm -rf "${UCXX_BUILD_DIR}"
    fi

    # Cleaning up python artifacts
    find "${REPODIR}/python/" | grep -E "(__pycache__|build|\.pyc|\.pyo|\.so|\_skbuild$)"  | xargs rm -rf

    set +x
fi

#------------------------------------------------------------------------------
if hasTarget uninstall; then
    INSTALL_MANIFEST_FILE=${LIBUCXX_BUILD_DIR}/install_manifest.txt
    if [ ! -e "${INSTALL_MANIFEST_FILE}" ]; then
        echo "Cannot find the install manifest file: ${INSTALL_MANIFEST_FILE}. Aborting"
        exit 1
    fi
    xargs -d '\n' rm -rf < "${INSTALL_MANIFEST_FILE}"
fi

#------------------------------------------------------------------------------
if hasTarget libucxx; then
    BUILD_TESTS=OFF; hasTarget libucxx-tests && BUILD_TESTS=ON
    BUILD_EXAMPLES=OFF; hasTarget libucxx-ex && BUILD_EXAMPLES="ON"
    BUILD_BENCHMARKS=OFF; hasTarget libucxx-bench && BUILD_BENCHMARKS="ON"
    BUILD_PY_API=OFF; hasTarget libucxx-py-api && BUILD_PY_API="ON"

    GENERATOR_ARG=""; which ninja && GENERATOR_ARG="-G Ninja"
    INSTALL_PREFIX_ARG=""
    if [[ -n "$INSTALL_PREFIX" ]]; then
        INSTALL_PREFIX_ARG="-DCMAKE_INSTALL_PREFIX=${INSTALL_PREFIX}"
    fi

    cmake -S "${REPODIR}/cpp" -B "${LIBUCXX_BUILD_DIR}" \
          "${GENERATOR_ARG}" \
          "${INSTALL_PREFIX_ARG}" \
          -DCMAKE_BUILD_TYPE="${BUILD_TYPE}" \
          -DBUILD_TESTS=${BUILD_TESTS} \
          -DBUILD_EXAMPLES=${BUILD_EXAMPLES} \
          -DBUILD_BENCHMARKS=${BUILD_BENCHMARKS} \
          -DUCXX_BENCHMARKS_ENABLE_CUDA=${BUILD_BENCHMARKS} \
          -DUCXX_BUILD_PYTHON_LIB=${BUILD_PY_API} \
          -DCMAKE_EXPORT_COMPILE_COMMANDS=${BUILD_COMPILE_COMMANDS} \
          -DUCXX_ENABLE_RMM=ON

    VERBOSE_ARG=""
    if (( VERBOSE )); then
        VERBOSE_ARG="-v"
    fi
    cmake --build "${LIBUCXX_BUILD_DIR}" -j "${PARALLEL_LEVEL}" ${VERBOSE_ARG}

    if (( ! NO_INSTALL )); then
        cmake --install "${LIBUCXX_BUILD_DIR}"
    fi
fi

#------------------------------------------------------------------------------
if hasTarget libucxx_py; then
    pushd "${REPODIR}/python/libucxx"

    CONFIG_SETTINGS=("skbuild.cmake.define.UCXX_ENABLE_RMM=ON")
    CONFIG_SETTINGS+=("skbuild.cmake.define.CMAKE_BUILD_TYPE=${BUILD_TYPE}")
    if [[ -n ${LIBUCXX_PY_BUILD_DIR} ]]; then
        CONFIG_SETTINGS+=("skbuild.build-dir=${LIBUCXX_PY_BUILD_DIR}/${WHEEL_TAG}")
    fi

    if (( NO_INSTALL )); then
        if [[ -n ${PYTHON_DIST_DIR} ]]; then
            OUTPUT_DIR_ARG="--outdir ${PYTHON_DIST_DIR}"
        fi
        python -m build --wheel --no-isolation --skip-dependency-check "${CONFIG_SETTINGS[@]/#/-C}" "${OUTPUT_DIR_ARG}"
    else
        CFG_EXPANDED=()
        for cfg_s in "${CONFIG_SETTINGS[@]}"; do
            CFG_EXPANDED+=("--config-settings" "${cfg_s}")
        done
        python -m pip install --no-build-isolation --no-deps "${CFG_EXPANDED[@]}" .
    fi

    popd
fi

#------------------------------------------------------------------------------
getCMakeInstallPrefix() {
    CMAKE_CACHE_PATH=${LIBUCXX_BUILD_DIR}/CMakeCache.txt
    cmake_prefix_path_line=$(grep '^CMAKE_PREFIX_PATH:PATH' "${CMAKE_CACHE_PATH}")
    printf %s "${cmake_prefix_path_line#*=}"
}

if hasTarget ucxx; then
    pushd "${REPODIR}/python/ucxx"

    CONFIG_SETTINGS=("skbuild.cmake.define.UCXX_ENABLE_RMM=ON")
    CONFIG_SETTINGS+=("skbuild.cmake.define.CMAKE_BUILD_TYPE=${BUILD_TYPE}")
    if (( FIND_LIBUCXX )); then
        CONFIG_SETTINGS+=("skbuild.cmake.define.FIND_UCXX_CPP=ON")
        CONFIG_SETTINGS+=("skbuild.cmake.define.FIND_UCXX_PYTHON=ON")
        CMAKE_PREFIX_PATH=${CMAKE_PREFIX_PATH}:$(getCMakeInstallPrefix):${LIBUCXX_BUILD_DIR}
        echo "CMAKE_PREFIX_PATH=${CMAKE_PREFIX_PATH}"
    else
        CONFIG_SETTINGS+=("skbuild.cmake.define.FIND_UCXX_CPP=ON")
        ucxx_DIR=${LIBUCXX_PY_BUILD_DIR:-${REPODIR}/python/libucxx/build}/${WHEEL_TAG}/ucxx_cpp
        CONFIG_SETTINGS+=("skbuild.cmake.define.ucxx_DIR=${ucxx_DIR}")
    fi
    if [[ -n ${UCXX_BUILD_DIR} ]]; then
        CONFIG_SETTINGS+=("skbuild.build-dir=${UCXX_BUILD_DIR}/${WHEEL_TAG}")
    fi
    if hasTarget ucxx-cython-tests; then
        CONFIG_SETTINGS+=("skbuild.cmake.define.UCXX_BUILD_TESTS=ON")
    fi

    if (( NO_INSTALL )); then
        if [[ -n ${PYTHON_DIST_DIR} ]]; then
            OUTPUT_DIR_ARG="--outdir ${PYTHON_DIST_DIR}"
        fi
        CMAKE_PREFIX_PATH=${CMAKE_PREFIX_PATH} \
        python -m build --wheel --no-isolation --skip-dependency-check "${CONFIG_SETTINGS[@]/#/-C}" "${OUTPUT_DIR_ARG}"
    else
        CFG_EXPANDED=()
        for cfg_s in "${CONFIG_SETTINGS[@]}"; do
            CFG_EXPANDED+=("--config-settings" "${cfg_s}")
        done
        CMAKE_PREFIX_PATH=${CMAKE_PREFIX_PATH} \
        python -m pip install --no-build-isolation --no-deps "${CFG_EXPANDED[@]}" .
    fi

    popd
fi

#------------------------------------------------------------------------------
if hasTarget distributed_ucxx; then
    pushd "${REPODIR}/python/distributed-ucxx"

    if (( NO_INSTALL )); then
        if [[ -n ${PYTHON_DIST_DIR} ]]; then
            OUTPUT_DIR_ARG="--outdir ${PYTHON_DIST_DIR}"
        fi
        python -m build --wheel --no-isolation --skip-dependency-check "${OUTPUT_DIR_ARG}"
    else
        python -m pip install --no-build-isolation --no-deps .
    fi

    popd
fi
