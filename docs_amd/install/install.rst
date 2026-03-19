.. SPDX-FileCopyrightText: Copyright (c) 2026 Advanced Micro Devices, Inc.
.. SPDX-License-Identifier: MIT

.. meta::
   :description: hipUCXX documentation and API reference library
   :keywords: UCX, UCXX, communication, networking, GPU-direct, RDMA, ROCm, ROCm-DS, AMD, HIP

Installing hipUCXX
==================

You can install hipUCXX via AMD PyPI as described below. This is recommended for users of the code. For developers interested in modifying or contributing to the Open Source hipUCXX component, see the :doc:`Build instructions <./build>`.

Requirements
------------

hipUCXX requires ROCm 7.2 running on a `ROCm-supported operating system <https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html#supported-operating-systems>`_. Using Ubuntu 22.04 or later is recommended.
For more information, see `ROCm-DS system requirements <https://rocm.docs.amd.com/projects/rocm-ds/en/latest/install/requirements.html>`_.

hipUCXX also requires a working installation of `UCX <https://www.openucx.org/>`_ (version 1.17.0 or later). UCX can be installed via your system package manager or built from source.

The steps in this topic require a Conda installation. A minimal free version of Conda is `Miniforge <https://conda-forge.org/download/>`_.

Install hipUCXX via AMD PyPI
-----------------------------

Packaged versions of hipUCXX and its dependencies are distributed via
`AMD PyPI <https://pypi.amd.com/simple>`_. This section discusses how to install
hipUCXX via this package index.

Create and activate a Conda environment with Python 3.12 as shown below:

.. code-block:: bash

   conda create --name hipucxx python=3.12
   conda activate hipucxx

hipUCXX can then be installed into this environment using pip and the AMD PyPI URL:

.. code-block:: bash

   pip install amd-hipucxx==0.1.0 --extra-index-url=https://pypi.amd.com/simple

This will also install the ``amd-libhipucxx`` dependency which provides the underlying C++ shared library.

To also install the Dask Distributed backend:

.. code-block:: bash

   pip install distributed-hipucxx==0.1.0 --extra-index-url=https://pypi.amd.com/simple
