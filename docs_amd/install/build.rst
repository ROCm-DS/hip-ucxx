.. meta::
  :description: hip-ucxx documentation and API reference library
  :keywords: UCX, UCXX, communication, networking, GPU-direct, RDMA, ROCm, ROCm-DS, AMD, HIP

.. _building-ucxx:

*****************************
Building hip-ucxx from source
*****************************

The following instructions provide steps to build and test hip-ucxx from source files provided in the
https://github.com/ROCm-DS/hip-ucxx repository. To install hip-ucxx for end users,
see :ref:`installing-ucxx`.

Requirements and dependencies
=============================

See :ref:`system-requirements` for information related to supported operating systems, ROCm versions,
and AMD GPUs before building hip-ucxx.

Building hip-ucxx uses the following tools and dependencies.

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Name
     - Version / Notes
   * - `cmake <https://cmake.org/>`_
     - ≥ 3.30.4
   * - `UCX <https://github.com/openucx/ucx>`_
     - ≥ 1.18.0 (must be built with ROCm support; see :ref:`building-ucx`)
   * - `hipMM (RMM) <https://github.com/ROCm-DS/hipMM>`_
     - 4.0.0 (required for GPU-to-GPU direct transfers)
   * - **Optional Dependencies**
     -
   * - `Googletest <https://github.com/google/googletest>`_
     - ≥ 1.13.0 (for tests)
   * - `Googlebench <https://github.com/google/benchmark>`_
     - (for benchmarks)
   * - `Doxygen <https://github.com/doxygen/doxygen>`_
     - ≥ 1.8.20 (for documentation)

.. note::

   ``hipMM`` provides GPU device memory management and is required for GPU buffer transfers
   via ``UCXXPyRMMBuffer``. Without it, only host memory transfers are supported. Most users
   working with GPU-to-GPU communication should install ``hipMM``.

Before building, set up the ROCm development environment so CMake can locate ROCm
libraries and headers. Export the following variables in the same shell session used
for ``./build.hip.sh`` or direct CMake invocations:

.. code-block:: bash

   export ROCM_PATH=/opt/rocm          # adjust if ROCm is installed elsewhere
   export CMAKE_PREFIX_PATH=${CMAKE_PREFIX_PATH}:${ROCM_PATH}

``/opt/rocm`` is the default ROCm install location. ``CMAKE_PREFIX_PATH`` is appended
to any existing value so previously configured prefixes are preserved.

.. _building-ucx:

Building UCX with ROCm support
==============================

hip-ucxx requires UCX built with ROCm support for GPU-direct communication.
Prebuilt system packages typically do not include this support, so building from
source is recommended.

Install the required system packages for RDMA/InfiniBand support:

**Ubuntu/Debian:**

.. code-block:: bash

   sudo apt install rdma-core libibverbs-dev librdmacm-dev libnuma-dev

**RHEL/CentOS:**

.. code-block:: bash

   sudo yum install rdma-core-devel libibverbs-devel librdmacm-devel numactl-devel

Download and extract the UCX source (replace ``1.18.0`` with the desired version):

.. code-block:: bash

   export UCX_VERSION=1.18.0
   wget -q "https://github.com/openucx/ucx/releases/download/v${UCX_VERSION}/ucx-${UCX_VERSION}.tar.gz"
   tar xzf "ucx-${UCX_VERSION}.tar.gz"

Configure and build:

.. code-block:: bash

   mkdir -p "ucx-${UCX_VERSION}/build"
   cd "ucx-${UCX_VERSION}/build"
   ../contrib/configure-release \
       --prefix=/usr \
       --with-rocm=/opt/rocm \
       --with-rc --with-ud --with-dm --with-rdmacm --with-verbs \
       --enable-mt --without-go --disable-assertions
   make -j$(nproc)
   sudo make install

Key configure flags:

- ``--with-rocm=/opt/rocm`` -- enables ROCm/HIP GPU support (adjust path if ROCm is installed elsewhere)
- ``--with-verbs`` -- InfiniBand Verbs API support (requires ``libibverbs-dev`` / ``libibverbs-devel``)
- ``--with-rdmacm`` -- RDMA Connection Manager support (requires ``librdmacm-dev`` / ``librdmacm-devel``)
- ``--with-rc --with-ud --with-dm`` -- Reliable Connected, Unreliable Datagram, and Device Memory transports
- ``--enable-mt`` -- multi-threading support (required for hip-ucxx)

See `UCX documentation <https://openucx.readthedocs.io/>`_ for additional configuration options.

Build and run scripts
=====================

The ``build.hip.sh`` and ``run.hip.sh`` scripts are the primary tools for building and running
hip-ucxx components. They handle build configuration, dependencies, and environment setup
automatically.

.. code-block:: bash

   ./build.hip.sh [options] [targets]
   ./run.hip.sh [options] [targets]

Build targets
-------------

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Target
     - Description
   * - ``clean``
     - Remove all existing build artifacts and start from a clean state
   * - ``all``
     - Build all targets
   * - **C++ targets**
     -
   * - ``libucxx``
     - Build the libucxx C++ library
   * - ``libucxx-tests``
     - Build C++ tests (implies ``libucxx``)
   * - ``libucxx-ex``
     - Build C++ examples (implies ``libucxx``)
   * - ``libucxx-bench``
     - Build C++ benchmarks (implies ``libucxx``)
   * - ``cxx-all``
     - Build all C++ targets
   * - **Python targets**
     -
   * - ``ucxx``
     - Build the ucxx Python module
   * - ``distributed_ucxx``
     - Build the Dask Distributed backend
   * - ``py-all``
     - Build all Python targets

Run targets
-----------

``run.hip.sh`` expects artifacts from a prior ``build.hip.sh`` invocation.

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Target
     - Description
   * - ``cpp_tests``
     - Run all C++ tests
   * - ``cpp_bench``
     - Run C++ benchmarks
   * - ``cpp_examples``
     - Run C++ examples
   * - ``py_tests``
     - Run Python core tests
   * - ``py_async_tests``
     - Run Python async tests
   * - ``py_bench``
     - Run Python core benchmarks
   * - ``py_async_bench``
     - Run Python async benchmarks

Run ``./build.hip.sh --help`` and ``./run.hip.sh --help`` for the full list of options
and targets.

C++ library
===========

Using CMake directly
--------------------

For more fine-grained control over the build, invoke CMake directly:

.. code-block:: bash

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

CMake build options:

.. list-table::
   :header-rows: 1
   :widths: 30 20 15 35

   * - Flag
     - Possible Values
     - Default Value
     - Behavior
   * - BUILD_TESTS
     - ON, OFF
     - ON
     - Compile C++ tests
   * - BUILD_BENCHMARKS
     - ON, OFF
     - OFF
     - Compile C++ benchmarks
   * - BUILD_EXAMPLES
     - ON, OFF
     - OFF
     - Compile C++ examples
   * - BUILD_SHARED_LIBS
     - ON, OFF
     - ON
     - Build shared libraries
   * - UCXX_ENABLE_RMM
     - ON, OFF
     - OFF
     - Enable hipMM support for GPU buffer transfers
   * - UCXX_BUILD_PYTHON_LIB
     - ON, OFF
     - OFF
     - Build Python API support library

Running C++ tests
-----------------

Using ``run.hip.sh`` (recommended):

.. code-block:: bash

   ./run.hip.sh cpp_tests

Alternatively, run tests directly with ctest:

.. code-block:: bash

   cd <UCXX_ROOT>/cpp/build
   ctest --test-dir ./tests

Python library
==============

Python environment and dependencies
-----------------------------------

Before building Python targets, activate a Conda or Python virtual environment
(see :ref:`installing-ucxx` for environment setup). Install the build-time Python
dependencies listed in ``python/requirements.txt``:

.. code-block:: bash

   pip install -r python/requirements.txt

The recommended way to build Python packages is with ``build.hip.sh``:

.. code-block:: bash

   # Build the ucxx Python module (includes libucxx)
   ./build.hip.sh ucxx

   # Build the Dask Distributed backend
   ./build.hip.sh distributed_ucxx

   # Build all Python targets
   ./build.hip.sh py-all

Building Python wheels manually
-------------------------------

For cases where ``build.hip.sh`` is not suitable, wheels can be built directly with pip:

.. code-block:: bash

   # Build and install libucxx Python module
   cd <UCXX_ROOT>/python/libucxx/
   pip wheel -w dist -v --no-build-isolation --disable-pip-version-check .
   pip install dist/libucxx-*.whl

   # Build and install ucxx Python module
   cd <UCXX_ROOT>/python/ucxx/
   pip wheel -w dist -v --no-build-isolation --disable-pip-version-check .
   pip install dist/ucxx-*.whl

Building documentation
======================

Prepare the environment to build documentation using the following commands:

.. code-block:: bash

   cd <UCXX_ROOT>
   pip install -r docs_amd/sphinx/requirements.txt

Build the documentation:

.. code-block:: bash

   cd <UCXX_ROOT>/docs_amd
   sphinx-build -b html . _build

Navigate to ``<UCXX_ROOT>/docs_amd/_build`` and open ``index.html`` to examine the generated documentation.
