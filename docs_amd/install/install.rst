.. SPDX-FileCopyrightText: Copyright (c) 2026 Advanced Micro Devices, Inc.
.. SPDX-License-Identifier: MIT

.. meta::
   :description: hip-ucxx documentation and API reference library
   :keywords: UCX, UCXX, communication, networking, GPU-direct, RDMA, ROCm, ROCm-DS, AMD, HIP

.. _installing-ucxx:

*******************
Installing hip-ucxx
*******************

You can install ``hip-ucxx`` via AMD PyPI as described below. This is recommended for users of the code. For developers interested in modifying or contributing to the Open Source ``hip-ucxx`` component, see the :ref:`building-ucxx`.

Requirements
============

See :ref:`system-requirements` for information related to supported operating systems, ROCm versions, and AMD GPUs before installing ``hip-ucxx``.

``hip-ucxx`` also requires a working installation of `UCX <https://www.openucx.org/>`_ (version 1.17.0 or later). UCX can be installed via your system package manager or built from source.

Install hip-ucxx via AMD PyPI
============================

Packaged versions of ``hip-ucxx`` and its dependencies are distributed via
`AMD PyPI <https://pypi.amd.com/simple>`_. This section discusses how to install
``hip-ucxx`` via this package index.

Create and activate a Conda environment with Python 3.12 as shown below:

.. code-block:: bash

   conda create --name hip-ucxx python=3.12
   conda activate hip-ucxx

hip-ucxx can then be installed into this environment using pip and the AMD PyPI URL:

.. code-block:: bash

   pip install amd-hip-ucxx==0.1.0 --extra-index-url=https://pypi.amd.com/simple

This will also install the ``amd-libhip-ucxx`` dependency which provides the underlying C++ shared library.

To also install the Dask Distributed backend:

.. code-block:: bash

   pip install distributed-hip-ucxx==0.1.0 --extra-index-url=https://pypi.amd.com/simple
