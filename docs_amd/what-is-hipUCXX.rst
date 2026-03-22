.. SPDX-FileCopyrightText: Copyright (c) 2026 Advanced Micro Devices, Inc.
.. SPDX-License-Identifier: MIT

*****************
What is hip-ucxx?
*****************

UCXX is a C++ wrapper library around `UCX <https://www.openucx.org/>`_ (Unified Communication X),
providing a modern object-oriented API for high-performance inter-process and inter-node
communication. UCX itself is a low-level C library for point-to-point networking that supports a
wide range of transports (InfiniBand, RoCE, shared memory, TCP, and more). UCXX adds C++
abstractions on top of the UCX C library making it significantly easier to build
communication-intensive applications.

``hip-ucxx`` is part of the AMD ROCm Data Science toolkit (ROCm-DS) and serves as the communication
layer for distributed GPU workloads in the ROCm-DS ecosystem. ``hip-ucxx`` is AMD's ROCm-native port
of the `NVIDIA RAPIDS UCXX <https://github.com/rapidsai/ucxx>`_ project. It has been adapted for the
HIP/ROCm stack while preserving the directory structure, file naming, and API naming to minimize
porting friction for developers working with both NVIDIA and AMD platforms.

Key highlights in ``hip-ucxx`` v0.1.0 include:

* Full integration with the ROCm-DS ecosystem. ``hip-ucxx`` serves as the communication layer for
  distributed GPU computing across ROCm-DS components.
* Multiple transport methods:

  - *Tag matching*: Tagged send/receive for message-based communication with sender-receiver coordination.
  - *Stream*: Ordered byte-stream communication over an endpoint.
  - *Active messages (AM)*: Enables execution of user-defined callbacks on the receiver side upon message arrival.
  - *Remote memory access (RMA/RDMA)*: Direct memory read/write operations across processes without involving the remote CPU.

* GPU-direct communication enables GPU-to-GPU direct data transfers without staging through host memory,
  reducing latency and increasing throughput.
* Python async API built on ``asyncio`` and a drop-in Dask Distributed backend (``distributed-ucxx``)
  that enables Dask to use UCX for inter-worker communication in distributed GPU computing pipelines.
* Supports hipMM device buffers for efficient GPU memory management during transfers.

Modules
-------

The following table summarizes the C++ modules available in ``hip-ucxx``:

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Module
     - Headers
     - Description

   * - :doc:`Core <./reference/cpp_api/core>`
     - `cpp/include/ucxx/context.h <https://github.com/AMD-AIOSS/hip-ucxx/blob/amd-integration/cpp/include/ucxx/context.h>`_, `worker.h <https://github.com/AMD-AIOSS/hip-ucxx/blob/amd-integration/cpp/include/ucxx/worker.h>`_, `address.h <https://github.com/AMD-AIOSS/hip-ucxx/blob/amd-integration/cpp/include/ucxx/address.h>`_, `config.h <https://github.com/AMD-AIOSS/hip-ucxx/blob/amd-integration/cpp/include/ucxx/config.h>`_, `component.h <https://github.com/AMD-AIOSS/hip-ucxx/blob/amd-integration/cpp/include/ucxx/component.h>`_
     - UCP context, worker, and address management. Configuration handling, base component class, and logging.

   * - :doc:`Communication <./reference/cpp_api/communication>`
     - `cpp/include/ucxx/endpoint.h <https://github.com/AMD-AIOSS/hip-ucxx/blob/amd-integration/cpp/include/ucxx/endpoint.h>`_, `listener.h <https://github.com/AMD-AIOSS/hip-ucxx/blob/amd-integration/cpp/include/ucxx/listener.h>`_
     - UCP endpoint and listener management for establishing and accepting connections.

   * - :doc:`Request <./reference/cpp_api/request>`
     - `cpp/include/ucxx/request_tag.h <https://github.com/AMD-AIOSS/hip-ucxx/blob/amd-integration/cpp/include/ucxx/request_tag.h>`_, `request_stream.h <https://github.com/AMD-AIOSS/hip-ucxx/blob/amd-integration/cpp/include/ucxx/request_stream.h>`_, `request_am.h <https://github.com/AMD-AIOSS/hip-ucxx/blob/amd-integration/cpp/include/ucxx/request_am.h>`_, `request_mem.h <https://github.com/AMD-AIOSS/hip-ucxx/blob/amd-integration/cpp/include/ucxx/request_mem.h>`_
     - Non-blocking send/receive operations via tag, stream, active message, and remote memory access APIs. Also includes flush and endpoint close requests.

   * - :doc:`Memory <./reference/cpp_api/memory>`
     - `cpp/include/ucxx/buffer.h <https://github.com/AMD-AIOSS/hip-ucxx/blob/amd-integration/cpp/include/ucxx/buffer.h>`_, `memory_handle.h <https://github.com/AMD-AIOSS/hip-ucxx/blob/amd-integration/cpp/include/ucxx/memory_handle.h>`_, `remote_key.h <https://github.com/AMD-AIOSS/hip-ucxx/blob/amd-integration/cpp/include/ucxx/remote_key.h>`_
     - Buffer types (host and hipMM device buffers), memory handle registration for RMA, and remote key management.

   * - :doc:`Async <./reference/cpp_api/async>`
     - `cpp/include/ucxx/future.h <https://github.com/AMD-AIOSS/hip-ucxx/blob/amd-integration/cpp/include/ucxx/future.h>`_, `notifier.h <https://github.com/AMD-AIOSS/hip-ucxx/blob/amd-integration/cpp/include/ucxx/notifier.h>`_, `delayed_submission.h <https://github.com/AMD-AIOSS/hip-ucxx/blob/amd-integration/cpp/include/ucxx/delayed_submission.h>`_
     - Future-based asynchronous completion tracking, request notification, delayed request submission, and worker progress thread management.

   * - :doc:`Utilities <./reference/cpp_api/utils>`
     - `cpp/include/ucxx/typedefs.h <https://github.com/AMD-AIOSS/hip-ucxx/blob/amd-integration/cpp/include/ucxx/typedefs.h>`_, `header.h <https://github.com/AMD-AIOSS/hip-ucxx/blob/amd-integration/cpp/include/ucxx/header.h>`_, `exception.h <https://github.com/AMD-AIOSS/hip-ucxx/blob/amd-integration/cpp/include/ucxx/exception.h>`_
     - Type definitions, multi-buffer header metadata, exception handling, and miscellaneous helper utilities (socket address, file descriptor, UCX wrappers).
