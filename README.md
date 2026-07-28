# hip-ucxx

hip-ucxx is an object-oriented C++ interface for [UCX](https://www.openucx.org/),
with native Python bindings, designed for GPU-direct communication on AMD GPUs
using HIP/ROCm. It is derived from the
[UCXX](https://github.com/rapidsai/ucxx) project by NVIDIA Corporation
and is part of the [AMD Data Science](https://github.com/AMD-Ecosystem/ROCm-DS) ecosystem.

hip-ucxx supports multiple transport methods including tag matching, active
messages, and stream-based communication over InfiniBand, ROCm-IPC/XGMI, shared
memory, and TCP. It also provides a Dask Distributed communication backend for
GPU-accelerated distributed computing.

For full documentation, see the
[hip-ucxx documentation](https://rocm.docs.amd.com/projects/hip-ucxx/en/latest/).

## Directory layout

```
hip-ucxx/
├── cpp/                  C++ library
│   ├── include/ucxx/       Public headers
│   ├── src/                Implementation
│   ├── tests/              C++ tests
│   ├── benchmarks/         C++ benchmarks
│   ├── examples/           C++ examples (basic client/server)
│   └── python/             C++ sources for Python bindings
├── python/               Python packages
│   ├── ucxx/               Core Python module (ucxx.core, ucxx._lib_async)
│   ├── libucxx/            Python wrapper that loads the C++ shared library
│   └── distributed-ucxx/   Dask Distributed communication backend
├── docs_amd/             Sphinx documentation source
├── cmake/                CMake helper modules
├── scripts/              Utility scripts (SPDX checks)
├── build.hip.sh          Build script for C++ and Python components
└── run.hip.sh            Run script for tests, benchmarks, and examples
```

## Environment setup

Create and activate a Python environment before building or installing
hip-ucxx. Either Conda or a Python virtual environment can be used.

**Conda:**

```bash
conda create --name hip-ucxx python=3.12
conda activate hip-ucxx
```

**Python virtual environment:**

```bash
python3 -m venv hip-ucxx-env
source hip-ucxx-env/bin/activate
```

For installing pre-built packages via AMD PyPI, see the
[installation guide](https://rocm.docs.amd.com/projects/hip-ucxx/en/latest/install/install.html).

## Dependencies

hip-ucxx requires UCX (≥ 1.18.0) built with ROCm support. Pre-built system
packages typically do not include ROCm support, so building from source is
recommended.

Install the RDMA/InfiniBand system packages first:

```bash
# Ubuntu/Debian
sudo apt install rdma-core libibverbs-dev librdmacm-dev libnuma-dev

# RHEL/CentOS
sudo yum install rdma-core-devel libibverbs-devel librdmacm-devel numactl-devel
```

Then build UCX with ROCm support:

```bash
export UCX_VERSION=1.18.0
wget -q "https://github.com/openucx/ucx/releases/download/v${UCX_VERSION}/ucx-${UCX_VERSION}.tar.gz"
tar xzf "ucx-${UCX_VERSION}.tar.gz"
mkdir -p "ucx-${UCX_VERSION}/build"
cd "ucx-${UCX_VERSION}/build"
../contrib/configure-release \
    --prefix=/usr \
    --with-rocm=/opt/rocm \
    --with-rc --with-ud --with-dm --with-rdmacm --with-verbs \
    --enable-mt --without-go --disable-assertions
make -j$(nproc)
sudo make install
```

[hipMM](https://github.com/AMD-Ecosystem/hipMM) is highly recommended for GPU-to-GPU
direct transfers.

For detailed dependency information and build options, see the
[build guide](https://rocm.docs.amd.com/projects/hip-ucxx/en/latest/install/build.html).

## Building and running

The `build.hip.sh` and `run.hip.sh` scripts are the primary tools for building
and running hip-ucxx components.

```bash
# ROCm development environment (adjust path if ROCm is installed elsewhere)
export ROCM_PATH=/opt/rocm
export CMAKE_PREFIX_PATH=${CMAKE_PREFIX_PATH}:${ROCM_PATH}

# Python build dependencies (activate your env first; see Environment setup above)
# Edit python/requirements.txt extra-index-url if your ROCm version differs from 7.2.3
pip install -r python/requirements.txt

# Build the C++ library
./build.hip.sh libucxx

# Build the Python module (includes libucxx)
./build.hip.sh ucxx

# Build everything
./build.hip.sh all

# Run C++ tests
./run.hip.sh cpp_tests

# Run Python tests
./run.hip.sh py_tests
```

Run `./build.hip.sh --help` and `./run.hip.sh --help` for the full list of
targets and options.

For advanced build options including direct CMake usage and manual wheel
building, see the
[build guide](https://rocm.docs.amd.com/projects/hip-ucxx/en/latest/install/build.html).

## Logging

Logging is independently available for both C++ and Python APIs. Since the
Python interface uses the C++ backend, C++ logging can be enabled when running
Python code as well.

### C++

The C++ interface reuses the UCX logger and provides the same log levels. It
can be enabled via the `UCXX_LOG_LEVEL` environment variable. This will not
enable UCX logging; set `UCX_LOG_LEVEL` separately for that.

```bash
# Request trace log level
UCXX_LOG_LEVEL=TRACE_REQ

# Debug log level
UCXX_LOG_LEVEL=DEBUG
```

### Python

The Python interface uses Python's `logging` library. The levels `INFO` and
`DEBUG` are available and can be enabled via the `UCXPY_LOG_LEVEL` environment
variable.

```bash
# Enable Python info log level
UCXPY_LOG_LEVEL=INFO

# Enable Python debug, UCXX request trace, and UCX data log levels together
UCXPY_LOG_LEVEL=DEBUG UCXX_LOG_LEVEL=TRACE_REQ UCX_LOG_LEVEL=DATA
```

## License

hip-ucxx is licensed under a combination of the BSD 3-Clause License (for code
derived from NVIDIA UCXX) and the MIT License (for AMD additions). See
[LICENSES/](LICENSES/) for the full license texts.
