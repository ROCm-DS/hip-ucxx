.. SPDX-FileCopyrightText: Copyright (c) 2026 Advanced Micro Devices, Inc.
.. SPDX-License-Identifier: MIT

.. meta::
  :description: hip-ucxx documentation and API reference library
  :keywords: UCX, UCXX, communication, networking, GPU-direct, RDMA, ROCm, ROCm-DS, AMD, HIP

.. _hip-ucxx:

********************************************************************
hip-ucxx documentation
********************************************************************

hip-ucxx is a C++ wrapper library around `UCX <https://www.openucx.org/>`_ (Unified Communication X), providing a modern object-oriented API for high-performance inter-process and inter-node communication on AMD GPUs. It is part of the AMD ROCm Data Science toolkit (ROCm-DS), an open-source software collection for high-performance data science applications. Forked from the NVIDIA® RAPIDS® UCXX project, hip-ucxx brings the same communication capabilities to the :doc:`HIP <hip:index>`/:doc:`ROCm <rocm:index>` stack. It offers both a modern C++ interface for systems developers and Python bindings with full async support for rapid prototyping and distributed computing workflows. For more information, see :doc:`What is hip-ucxx? <what-is-hip-ucxx>`

The hip-ucxx code is open and hosted at `https://github.com/AMD-AIOSS/hip-ucxx <https://github.com/AMD-AIOSS/hip-ucxx>`_.

.. grid:: 2
  :gutter: 3

  .. grid-item-card:: Installation

    * :doc:`System requirements <install/system-requirements>`
    * :doc:`Installing hip-ucxx <install/install>`
    * :doc:`Building hip-ucxx <install/build>`

  .. grid-item-card:: How to

    * :doc:`Use hip-ucxx <how-to/using-hip-ucxx>`
    * :doc:`Configure hip-ucxx <how-to/configuration>`
    * :doc:`Optimization <how-to/optimization>`
    * :doc:`Deployment <how-to/deployment>`

  .. grid-item-card:: API reference

    * :ref:`C++ API reference <hip-ucxx-cpp>`
    * :ref:`Python API reference <hip-ucxx-python>`

To contribute to the documentation refer to `Contributing to ROCm-DS  <https://rocm.docs.amd.com/projects/rocm-ds/en/latest/contribute/contributing.html>`_.

You can find licensing information on the `Licensing <https://rocm.docs.amd.com/projects/rocm-ds/en/latest/about/license.html>`_ page.
