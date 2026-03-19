.. SPDX-FileCopyrightText: Copyright (c) 2026 Advanced Micro Devices, Inc.
.. SPDX-License-Identifier: MIT

What is hipUCXX?
================

Overview
--------

UCXX is a C++ wrapper library around `UCX <https://www.openucx.org/>`_ (Unified Communication X), providing a modern object-oriented API for high-performance inter-process and inter-node communication. UCX itself is a low-level C library for point-to-point networking that supports a wide range of transports (InfiniBand, RoCE, shared memory, TCP, and more). UCXX adds C++ abstractions on top — including RAII resource management, smart pointers, futures, and asynchronous request tracking — making it significantly easier to build communication-intensive applications.

UCXX supports multiple transport methods:

- **Tag matching** – Tagged send/receive for message-based communication with sender-receiver coordination.
- **Stream** – Ordered byte-stream communication over an endpoint.
- **Active messages (AM)** – Enables execution of user-defined callbacks on the receiver side upon message arrival.
- **Remote memory access (RMA/RDMA)** – Direct memory read/write operations across processes without involving the remote CPU.

UCXX also enables **GPU-direct communication**, allowing GPU memory to be sent and received directly without staging through host memory. This is critical for high-performance distributed GPU computing workloads.

The library includes a full **Python async API** built on asyncio, as well as a **Dask Distributed backend** (``distributed-ucxx``) that enables Dask to use UCX for inter-worker communication in distributed GPU computing pipelines.

AMD ROCm port
-------------

hipUCXX is AMD's ROCm-native port of the `NVIDIA RAPIDS UCXX <https://github.com/rapidsai/ucxx>`_ project. It has been adapted for the HIP/ROCm stack while preserving the directory structure, file naming, and API naming to minimize porting friction for developers working with both NVIDIA and AMD platforms. hipUCXX is part of the AMD ROCm Data Science toolkit (ROCm-DS) and serves as the communication layer for distributed GPU workloads in the ROCm-DS ecosystem.

Modules
-------

The following table summarizes the C++ modules available in hipUCXX:

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Module
     - Headers
     - Description
   * - `Core <./reference/cpp_api/core.html>`_
     - `cpp/include/ucxx/context.h <https://github.com/AMD-AIOSS/hipUCXX/tree/main/cpp/include/ucxx/context.h>`_, `worker.h <https://github.com/AMD-AIOSS/hipUCXX/tree/main/cpp/include/ucxx/worker.h>`_, `address.h <https://github.com/AMD-AIOSS/hipUCXX/tree/main/cpp/include/ucxx/address.h>`_, `config.h <https://github.com/AMD-AIOSS/hipUCXX/tree/main/cpp/include/ucxx/config.h>`_, `component.h <https://github.com/AMD-AIOSS/hipUCXX/tree/main/cpp/include/ucxx/component.h>`_
     - UCP context, worker, and address management. Configuration handling, base component class, and logging.
   * - `Communication <./reference/cpp_api/communication.html>`_
     - `cpp/include/ucxx/endpoint.h <https://github.com/AMD-AIOSS/hipUCXX/tree/main/cpp/include/ucxx/endpoint.h>`_, `listener.h <https://github.com/AMD-AIOSS/hipUCXX/tree/main/cpp/include/ucxx/listener.h>`_
     - UCP endpoint and listener management for establishing and accepting connections.
   * - `Request <./reference/cpp_api/request.html>`_
     - `cpp/include/ucxx/request_tag.h <https://github.com/AMD-AIOSS/hipUCXX/tree/main/cpp/include/ucxx/request_tag.h>`_, `request_stream.h <https://github.com/AMD-AIOSS/hipUCXX/tree/main/cpp/include/ucxx/request_stream.h>`_, `request_am.h <https://github.com/AMD-AIOSS/hipUCXX/tree/main/cpp/include/ucxx/request_am.h>`_, `request_mem.h <https://github.com/AMD-AIOSS/hipUCXX/tree/main/cpp/include/ucxx/request_mem.h>`_
     - Non-blocking send/receive operations via tag, stream, active message, and remote memory access APIs. Also includes flush and endpoint close requests.
   * - `Memory <./reference/cpp_api/memory.html>`_
     - `cpp/include/ucxx/buffer.h <https://github.com/AMD-AIOSS/hipUCXX/tree/main/cpp/include/ucxx/buffer.h>`_, `memory_handle.h <https://github.com/AMD-AIOSS/hipUCXX/tree/main/cpp/include/ucxx/memory_handle.h>`_, `remote_key.h <https://github.com/AMD-AIOSS/hipUCXX/tree/main/cpp/include/ucxx/remote_key.h>`_
     - Buffer types (host and RMM device buffers), memory handle registration for RMA, and remote key management.
   * - `Async <./reference/cpp_api/async.html>`_
     - `cpp/include/ucxx/future.h <https://github.com/AMD-AIOSS/hipUCXX/tree/main/cpp/include/ucxx/future.h>`_, `notifier.h <https://github.com/AMD-AIOSS/hipUCXX/tree/main/cpp/include/ucxx/notifier.h>`_, `delayed_submission.h <https://github.com/AMD-AIOSS/hipUCXX/tree/main/cpp/include/ucxx/delayed_submission.h>`_
     - Future-based asynchronous completion tracking, request notification, delayed request submission, and worker progress thread management.
   * - `Utilities <./reference/cpp_api/utils.html>`_
     - `cpp/include/ucxx/typedefs.h <https://github.com/AMD-AIOSS/hipUCXX/tree/main/cpp/include/ucxx/typedefs.h>`_, `header.h <https://github.com/AMD-AIOSS/hipUCXX/tree/main/cpp/include/ucxx/header.h>`_, `exception.h <https://github.com/AMD-AIOSS/hipUCXX/tree/main/cpp/include/ucxx/exception.h>`_
     - Type definitions, multi-buffer header metadata, exception handling, and miscellaneous helper utilities (socket address, file descriptor, UCX wrappers).
