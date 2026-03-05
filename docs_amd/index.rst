.. SPDX-FileCopyrightText: Copyright (c) 2026 Advanced Micro Devices, Inc.
.. SPDX-License-Identifier: MIT

.. meta::
  :description: hipUCXX documentation and API reference library
  :keywords: UCX, UCXX, communication, networking, GPU-direct, RDMA, ROCm, ROCm-DS, AMD, HIP

.. _hipucxx:

********************************************************************
hipUCXX documentation
********************************************************************

hipUCXX is a C++ wrapper library around `UCX <https://www.openucx.org/>`_ (Unified Communication X), providing a modern object-oriented API for high-performance inter-process and inter-node communication on AMD GPUs. It is part of the AMD ROCm Data Science toolkit (ROCm-DS), an open-source software collection for high-performance data science applications. Forked from the NVIDIA® RAPIDS® UCXX project, hipUCXX brings the same communication capabilities to the :doc:`HIP <hip:index>`/:doc:`ROCm <rocm:index>` stack while preserving the directory structure, file naming, and API naming, to minimize porting friction for developers using both projects. It offers both a modern C++ interface for systems developers and Python bindings with full async support for rapid prototyping and distributed computing workflows. For more information, see :doc:`What is hipUCXX? <what-is-hipUCXX>`

Key highlights in hipUCXX v0.1.0 include:

* Full integration with the ROCm-DS ecosystem – Serves as the communication layer for distributed GPU computing across ROCm-DS components.
* Modern C++ API with RAII and smart pointers – Wraps the low-level UCX C API with type-safe, object-oriented C++ abstractions including automatic resource management.
* Multiple transport methods – Supports tag matching, stream, active messages (AM), and remote memory access (RMA/RDMA) for flexible communication patterns.
* GPU-direct communication – Enables direct GPU-to-GPU data transfers without staging through host memory, reducing latency and increasing throughput.
* Python async API and Dask Distributed backend – Provides full asyncio-based Python bindings and a drop-in Dask Distributed communication backend for distributed GPU computing.
* Optional RMM integration – Supports RMM (RAPIDS Memory Manager) device buffers for efficient GPU memory management during transfers.

The hipUCXX code is open and hosted at `https://github.com/AMD-AIOSS/hipUCXX <https://github.com/AMD-AIOSS/hipUCXX>`_.

.. grid:: 2
  :gutter: 3

  .. grid-item-card:: Installation

    * :doc:`Installing hipUCXX <install/install>`
    * :doc:`Building hipUCXX <install/build>`

  .. grid-item-card:: How to

    * :doc:`Use hipUCXX <how-to/using-hipUCXX>`

  .. grid-item-card:: API reference

    * :ref:`C++ API reference <hipucxx-cpp>`
    * :ref:`Python API reference <hipucxx-python>`


To contribute to the documentation refer to `Contributing to ROCm-DS  <https://rocm.docs.amd.com/projects/rocm-ds/en/latest/contribute/contributing.html>`_.

You can find licensing information on the `Licensing <https://rocm.docs.amd.com/projects/rocm-ds/en/latest/about/license.html>`_ page.
