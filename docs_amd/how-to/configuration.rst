.. SPDX-FileCopyrightText: Copyright (c) 2026 Advanced Micro Devices, Inc.
.. SPDX-License-Identifier: MIT

Configuration
=============

UCX/hipUCXX can be configured with a wide variety of options and optimizations including: transport, caching, etc. Users can configure UCX/hipUCXX either with environment variables or programmatically during initialization. Below we demonstrate setting ``UCX_MEMTYPE_CACHE`` to ``n`` and checking the configuration:

.. code-block:: python

   import ucxx
   options = {"PROTO_INFO": "y"}
   ucxx.init(options)
   assert ucxx.get_config()['PROTO_INFO'] == 'y'

.. note::
   When programmatically configuring hipUCXX, the ``UCX`` prefix is not used.

For novice users we recommend using hipUCXX defaults, see the next section for details.

hipUCXX vs UCX defaults
-----------------------

hipUCXX redefines some of the UCX defaults for a variety of reasons, including better performance for the more common Python use cases, or to work around known limitations or bugs of UCX. To verify UCX default configurations, for the currently installed UCX version please run the command-line tool ``ucx_info -f``.

Below is a list of the hipUCXX redefined default values, and what conditions are required for them to apply.

Apply to all UCX versions::

   UCX_MEMTYPE_CACHE=n
   UCX_RNDV_THRESH=8192
   UCX_FRAG_MEM_TYPE=rocm
   UCX_MAX_RNDV_RAILS=1

Apply to UCX < 1.18.0, newer versions rely on UCX defaults::

   UCX_PROTO_ENABLE=n

UCX environment variables in hipUCXX
------------------------------------

In this section we go over a brief overview of some of the more relevant variables for current hipUCXX usage, along with some comments on their uses and limitations. To see a complete list of UCX environment variables, their descriptions and default values, please run the command-line tool ``ucx_info -f``.

UCP context configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^

Configuration variables applying to the UCP context.

UCX_PROTO_ENABLE
"""""""""""""""""

Values: ``y``, ``n``

Enable the new protocol selection logic, also known as "protov2". Its default has been changed to ``y`` starting with UCX 1.16.0.

The new protocol solves various limitations from the original "protov1" including, for example, invalid choice of transport in systems with hybrid interconnectivity, such as systems where only a subset of GPU pairs are interconnected via XGMI.

Debug
^^^^^

Debug variables for both UCX and hipUCXX can be set.

UCXPY_LOG_LEVEL / UCX_LOG_LEVEL
""""""""""""""""""""""""""""""""

Values: ``DEBUG``, ``TRACE``

If UCX has been built with debug mode enabled.

Memory
^^^^^^

UCX_MEMTYPE_CACHE
"""""""""""""""""

This is a UCX Memory optimization which toggles whether UCX library intercepts memory allocation calls. hipUCXX defaults this value to ``n``. There are `known issues <https://github.com/openucx/ucx/wiki/NVIDIA-GPU-Support#known-issues>`_ when using this feature.

Values: ``n`` / ``y``

UCX_ROCM_IPC_CACHE
""""""""""""""""""

This is a UCX ROCm Memory optimization which enables/disables a remote endpoint IPC memhandle mapping cache. UCX/hipUCXX defaults this value to ``y``.

Values: ``n`` / ``y``

UCX_MEMTYPE_REG_WHOLE_ALLOC_TYPES
""""""""""""""""""""""""""""""""""

By defining ``UCX_MEMTYPE_REG_WHOLE_ALLOC_TYPES=rocm`` (default in UCX >= 1.12.0), UCX enables registration cache based on a buffer's base address, thus preventing multiple time-consuming registrations for the same buffer. This is particularly useful when using a GPU memory pool, thus requiring a single registration between two ends for the entire pool, providing considerable performance gains, especially when using InfiniBand.

Transports
^^^^^^^^^^

UCX_MAX_RNDV_RAILS
""""""""""""""""""

Limiting the number of rails (network devices) to ``1`` allows UCX to use only the closest device according to NUMA locality and system topology. Particularly useful with InfiniBand and AMD GPUs, ensuring all transfers from/to the GPU will use the closest InfiniBand device and thus implicitly enable GPUDirectRDMA.

.. note::
   On CPU-only systems, better network bandwidth performance with InfiniBand transports may be achieved by letting UCX use more than a single network device. This can be achieved by explicitly setting ``UCX_MAX_RNDV_RAILS`` to ``2`` or higher.

Values: Int (hipUCXX default: ``1``)

UCX_RNDV_THRESH
"""""""""""""""

This is a configurable parameter used by UCX to help determine which transport method should be used. For example, on machines with multiple GPUs, and with ROCm-IPC enabled, UCX can deliver messages either through TCP or ROCm-IPC. Sending GPU buffers over TCP is costly as it triggers a device-to-host on the sender side, and then host-to-device transfer on the receiver side -- we want to avoid these kinds of transfers when ROCm-IPC is available. If a buffer is below the threshold, `Rendezvous Protocol <https://github.com/openucx/ucx/wiki/Rendezvous-Protocol>`_ is triggered and for hipUCXX users, this will typically mean messages will be delivered through TCP. Depending on the application, messages can be quite small, therefore, we recommend setting a small value if the application uses ROCm-IPC or InfiniBand: ``UCX_RNDV_THRESH=8192``

Values: Int (hipUCXX default: ``8192``)

UCX_RNDV_SCHEME
"""""""""""""""

Communication scheme in RNDV protocol.

Values:

- ``put_zcopy``
- ``get_zcopy``
- ``auto`` (default)

UCX_TCP_RX_SEG_SIZE
"""""""""""""""""""

Size of send copy-out buffer when receiving. This environment variable controls the size of the buffer on the host when receiving data over TCP.

UCX_TCP_TX_SEG_SIZE
"""""""""""""""""""

Size of send copy-out buffer when transmitting. This environment variable controls the size of the buffer on the host when sending data over TCP.

.. note::
   Users should take care to properly tune ``UCX_TCP_{RX/TX}_SEG_SIZE`` parameters when mixing TCP with other transport methods as well as when using TCP over UCX in isolation. These variables will impact ROCm transfers when no ROCm-IPC or InfiniBand is available between hipUCXX processes. These parameters will cause the HostToDevice and DeviceToHost copies of buffers to be broken down in several chunks when the size of a buffer exceeds the size defined by these two variables. If an application is expected to transfer very large buffers, increasing such values may improve overall performance.

UCX_TLS
"""""""

Transport Methods (Simplified):

- ``all`` -- use all the available transports
- ``rc`` -- InfiniBand (``ibv_post_send``, ``ibv_post_recv``, ``ibv_poll_cq``) uses ``rc_v`` and ``rc_x`` (preferably if available)
- ``rocm_copy`` -- ROCm host-device memory copies
- ``rocm_ipc`` -- ROCm Inter-Process Communication (for GPU-to-GPU transfers between processes on the same node)
- ``sm`` / ``shm`` -- all shared memory transports (``mm``, ``cma``, ``knem``)
- ``mm`` -- shared memory transports - only memory mappers
- ``ugni`` -- ``ugni_smsg`` and ``ugni_rdma`` (uses ``ugni_udt`` for bootstrap)
- ``ib`` -- all InfiniBand transports (``rc``/``rc_mlx5``, ``ud``/``ud_mlx5``, ``dc_mlx5``)
- ``rc_v`` -- rc verbs (uses ``ud`` for bootstrap)
- ``rc_x`` -- rc with accelerated verbs (uses ``ud_mlx5`` for bootstrap)
- ``ud_v`` -- ud verbs
- ``ud_x`` -- ud with accelerated verbs
- ``ud`` -- ``ud_v`` and ``ud_x`` (preferably if available)
- ``dc`` / ``dc_x`` -- dc with accelerated verbs
- ``tcp`` -- sockets over TCP/IP
- ``rocm`` -- ROCm (AMD GPU) memory support

SOCKADDR_TLS_PRIORITY
"""""""""""""""""""""

Priority of sockaddr transports.

InfiniBand device
^^^^^^^^^^^^^^^^^

Select InfiniBand Device.

UCX_NET_DEVICES
"""""""""""""""

It's recommended to not define this variable and instead let UCX determine the closest InfiniBand device. Note that this requires the HIP/ROCm context to be created **before UCX/hipUCXX are initialized**.

Typically these will be the InfiniBand device corresponding to a particular set of GPUs. Values:

- Check ``ucx_info -d`` for a complete list

To find more information on the topology of InfiniBand-GPU pairing run the following:

.. code-block:: bash

   rocm-smi --showtopo

Example configs
---------------

InfiniBand -- No ROCm-IPC
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   UCX_TLS=rc,tcp,rocm_copy <SCRIPT>

InfiniBand -- With ROCm-IPC
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   UCX_TLS=rc,tcp,rocm_copy,rocm_ipc <SCRIPT>

TLS/Socket -- No ROCm-IPC
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   UCX_TLS=tcp,rocm_copy <SCRIPT>

TLS/Socket -- With ROCm-IPC
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   UCX_TLS=tcp,rocm_copy,rocm_ipc <SCRIPT>
