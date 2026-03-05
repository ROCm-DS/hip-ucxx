<!-- SPDX-FileCopyrightText: Copyright (c) 2026 Advanced Micro Devices, Inc. -->
<!-- SPDX-License-Identifier: MIT -->

# Building hipUCXX from source

hipUCXX provides C++ and Python APIs. The following instructions provide steps to build and test hipUCXX from source files provided in the [https://github.com/AMD-AIOSS/hipUCXX](https://github.com/AMD-AIOSS/hipUCXX) repository. To install hipUCXX for end users, see [Installing hipUCXX](./install.md).

## Tested on the following GPUs

| AMD Instinct GPU    | Architecture | Wavefront Size | LLVM target |
|---------------------|--------------|----------------|-------------|
| MI210               | CDNA2        | 64             | gfx90a      |
| MI250               | CDNA2        | 64             | gfx90a      |
| MI250X              | CDNA2        | 64             | gfx90a      |
| MI300A              | CDNA3        | 64             | gfx942      |
| MI300X              | CDNA3        | 64             | gfx942      |

## Dependencies

hipUCXX builds against the AMD ROCm software stack, that is the ROCm runtime, HIP compiler tool-chain, and a GPU driver that matches your ROCm version.

Install ROCm 7.2, or the minimum version supported by the GPUs listed above, and make sure the `rocminfo` and `hipcc` commands are in your `PATH`. For more information, see [ROCm Installation](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/).

| Name                                                                  | Version / Notes                              |
| ---------------------------------------------------------             | -------------------------------------------- |
| [`cmake`](https://cmake.org/)                                         | ≥ 3.26.4                                     |
| [`UCX`](https://github.com/openucx/ucx)                               | ≥ 1.17.0                                     |
| **Optional Dependencies**                                                                                            |
| [`hipMM (RMM)`](https://github.com/AMD-AIOSS/hipMM)                   | 4.0.0 (for GPU buffer support)               |
| [`Googletest`](https://github.com/google/googletest)                  | ≥ 1.13.0 (for tests)                         |
| [`Googlebench`](https://github.com/google/benchmark)                  | (for benchmarks)                             |
| [`Doxygen`](https://github.com/doxygen/doxygen)                       | ≥ 1.8.20 (for documentation)                |

## C++ library

### Building with `build.hip.sh`

The `build.hip.sh` script simplifies the build process. Use it to build the C++ library, tests, examples, and benchmarks.

```bash
# Build the libucxx C++ library
./build.hip.sh libucxx

# Build with tests
./build.hip.sh libucxx libucxx-tests

# Build with examples
./build.hip.sh libucxx libucxx-ex

# Build with benchmarks
./build.hip.sh libucxx libucxx-bench

# Build all C++ targets
./build.hip.sh cxx-all
```

### Using CMake directly

For more fine-grained control over the build, invoke CMake directly:

```bash
cd <UCXX_ROOT>/cpp
mkdir -p build && rm -rf build/*
cd build
cmake -S .. \
      -G Ninja \
      -B . \
      -DCMAKE_INSTALL_PREFIX=install \
      -DCMAKE_BUILD_TYPE=Release \
      -DBUILD_TESTS=ON \
      -DBUILD_EXAMPLES=ON
ninja
ninja install
```

CMake build options:

| Flag                      | Possible Values   | Default Value | Behavior                                           |
|---------------------------|-------------------|---------------|-----------------------------------------------------|
| BUILD_TESTS               | ON, OFF           | ON            | Compile C++ tests                                   |
| BUILD_BENCHMARKS          | ON, OFF           | OFF           | Compile C++ benchmarks                              |
| BUILD_EXAMPLES            | ON, OFF           | OFF           | Compile C++ examples                                |
| BUILD_SHARED_LIBS         | ON, OFF           | ON            | Build shared libraries                              |
| UCXX_ENABLE_RMM           | ON, OFF           | OFF           | Enable RMM support for GPU buffer transfers         |
| UCXX_BUILD_PYTHON_LIB     | ON, OFF           | OFF           | Build Python API support library                    |

### Running C++ tests

```bash
cd <UCXX_ROOT>/cpp/build
ctest --test-dir ./tests
```

## Python library

### Building Python packages with `build.hip.sh`

```bash
# Build the ucxx Python module (includes libucxx)
./build.hip.sh ucxx

# Build the Dask Distributed backend
./build.hip.sh distributed_ucxx

# Build all Python targets
./build.hip.sh py-all
```

### Building Python wheels manually

```bash
# Build and install libucxx Python module
cd <UCXX_ROOT>/python/libucxx/
pip wheel -w dist -v --no-build-isolation --disable-pip-version-check .
pip install dist/libucxx-*.whl

# Build and install ucxx Python module
cd <UCXX_ROOT>/python/ucxx/
pip wheel -w dist -v --no-build-isolation --disable-pip-version-check .
pip install dist/ucxx-*.whl
```

### Build options

The `build.hip.sh` script accepts additional options:

```bash
./build.hip.sh [options] [targets]
```

| Option              | Description                                              |
|---------------------|----------------------------------------------------------|
| `--build-dir`       | Specify a build directory (default is in-source)         |
| `--install-prefix`  | Specify an install prefix for the C++ library            |
| `--find-libucxx`    | Use an existing libucxx installation for the Python build|
| `--gpu-archs`       | GPU architectures: `native` (default), `rapids`, or list |
| `-j`                | Number of parallel build jobs                            |
| `-v`                | Verbose build output                                     |
| `-g`                | Build with debug settings                                |
| `-n`                | Skip install step                                        |
| `clean`             | Remove existing build artifacts                          |

## Building documentation

Prepare the environment to build documentation using the following commands:

```bash
cd <UCXX_ROOT>
pip install -r docs_amd/sphinx/requirements.txt
```

Build the documentation:

```bash
cd <UCXX_ROOT>/docs_amd
sphinx-build -b html . _build
```

Navigate to `<UCXX_ROOT>/docs_amd/_build` and open `index.html` to examine the generated documentation.
