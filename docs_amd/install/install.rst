.. meta::
   :description: hip-ucxx documentation and API reference library
   :keywords: UCX, UCXX, communication, networking, GPU-direct, RDMA, ROCm, ROCm-DS, AMD, HIP

.. _installing-ucxx:

*******************
Installing hip-ucxx
*******************

You can install hip-ucxx via AMD PyPI as described below. This is recommended for users of the
code. For developers interested in modifying or contributing to the Open Source hip-ucxx
component, see the :ref:`building-ucxx`.

Requirements
============

See :ref:`system-requirements` for information related to supported operating systems, ROCm versions,
and AMD GPUs before installing hip-ucxx.

hip-ucxx also requires a working installation of `UCX <https://www.openucx.org/>`_
(version 1.18.0 or later) built with ROCm support. See :ref:`building-ucx` for
instructions on building UCX from source with the required configuration.

Install hip-ucxx via AMD PyPI
============================

Packaged versions of hip-ucxx and its dependencies are distributed via
`AMD PyPI <https://pypi.amd.com/rocm-7.2.3/simple/>`_. This section discusses how to install
hip-ucxx via this package index.

Set up a Python environment
---------------------------

**Option A: Conda**

Create and activate a Conda environment with a compatible Python version, such as 3.11 or 3.12 as shown below. For more information on compatible Python versions, see :ref:`system-requirements`.

.. code-block:: bash

   conda create --name hip-ucxx python=3.12 # Specify your Python version
   conda activate hip-ucxx

**Option B: Python virtual environment**

Create and activate a virtual environment:

.. code-block:: bash

   python3 -m venv hip-ucxx-env
   source hip-ucxx-env/bin/activate

Install packages
----------------

With your environment activated, install hip-ucxx using pip and the AMD PyPI URL:

.. code-block:: bash

   pip install amd-hipucxx==0.1.0 --extra-index-url=https://pypi.amd.com/rocm-7.2.3/simple/

This will also install the ``amd-libhipucxx`` dependency, which provides the underlying C++ shared
library.

To also install the Dask Distributed backend:

.. code-block:: bash

   pip install amd-distributed-hipucxx==0.1.0 --extra-index-url=https://pypi.amd.com/rocm-7.2.3/simple/
