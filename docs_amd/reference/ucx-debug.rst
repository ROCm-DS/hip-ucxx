.. SPDX-FileCopyrightText: Copyright NVIDIA CORPORATION & AFFILIATES.
.. SPDX-FileCopyrightText: Copyright (c) 2026 Advanced Micro Devices, Inc.
.. SPDX-License-Identifier: BSD-3-Clause AND MIT

Debugging UCX
=============

InfiniBand
----------

System configuration
^^^^^^^^^^^^^^^^^^^^

``ibdev2netdev`` -- check to ensure at least one IB controller is configured for IPoIB:

.. code-block:: text

   $ ibdev2netdev
   mlx5_0 port 1 ==> ib0 (Up)
   mlx5_1 port 1 ==> ib1 (Up)
   mlx5_2 port 1 ==> ib2 (Up)
   mlx5_3 port 1 ==> ib3 (Up)

``ucx_info -d`` and ``ucx_info -p -u t`` are helpful commands to display what UCX understands about
the underlying hardware. For example, we can check if UCX has been built correctly with RDMA and if
it is available:

.. code-block:: bash

   $ ucx_info -d | grep -i rdma
   # Memory domain: rdmacm
   #     Component: rdmacm
   # Connection manager: rdmacm

.. code-block:: bash

   $ ucx_info -b | grep -i rdma
   #define HAVE_DECL_RDMA_ESTABLISH  1
   #define HAVE_DECL_RDMA_INIT_QP_ATTR 1
   #define HAVE_RDMACM_QP_LESS       1

InfiniBand performance
^^^^^^^^^^^^^^^^^^^^^^

``ucx_perftest`` should confirm InfiniBand bandwidth to be in the 10+ GB/s range:

.. code-block:: bash

   HIP_VISIBLE_DEVICES=0 UCX_NET_DEVICES=mlx5_0:1 UCX_TLS=rc,rocm_copy ucx_perftest -t tag_bw -m rocm -s 100000000 -n 10 -p 9999 &
   HIP_VISIBLE_DEVICES=1 UCX_NET_DEVICES=mlx5_1:1 UCX_TLS=rc,rocm_copy ucx_perftest $(hostname) -t tag_bw -m rocm -s 100000000 -n 10 -p 9999

.. code-block:: text

   +--------------+-----------------------------+---------------------+-----------------------+
   |              |       latency (usec)        |   bandwidth (MB/s)  |  message rate (msg/s) |
   +--------------+---------+---------+---------+----------+----------+-----------+-----------+
   | # iterations | typical | average | overall |  average |  overall |   average |   overall |
   +--------------+---------+---------+---------+----------+----------+-----------+-----------+
   +------------------------------------------------------------------------------------------+
   | API:          protocol layer                                                             |
   | Test:         tag match bandwidth                                                        |
   | Data layout:  (automatic)                                                                |
   | Send memory:  rocm                                                                       |
   | Recv memory:  rocm                                                                       |
   | Message size: 100000000                                                                  |
   +------------------------------------------------------------------------------------------+
                 10     0.000  9104.800  9104.800   10474.41   10474.41         110         110

``-c`` option is NUMA dependent and sets the CPU Affinity of process for a particular GPU.
CPU Affinity and topology information can be found with:

.. code-block:: bash

   amd-smi topology

ROCm-IPC / XGMI
---------------

System configuration
^^^^^^^^^^^^^^^^^^^^

To verify the GPU topology and interconnect on an AMD system:

.. code-block:: bash

   amd-smi topology

This shows the inter-GPU connectivity -- XGMI links (analogous to NVLink), PCIe connections, and NUMA
node assignments.

To check which GPUs are visible:

.. code-block:: bash

   amd-smi static

ROCm-IPC performance
^^^^^^^^^^^^^^^^^^^^

``ucx_perftest`` should confirm ROCm-IPC bandwidth. Performance will depend on interconnect type
(XGMI vs PCIe):

.. code-block:: bash

   HIP_VISIBLE_DEVICES=0 UCX_TLS=rocm_ipc,rocm_copy,tcp ucx_perftest -t tag_bw -m rocm -s 10000000 -n 10 -p 9999 &
   HIP_VISIBLE_DEVICES=1 UCX_TLS=rocm_ipc,rocm_copy,tcp ucx_perftest $(hostname) -t tag_bw -m rocm -s 100000000 -n 10 -p 9999

.. code-block:: text
Accepted connection from 127.0.0.1:37734
+--------------+--------------+------------------------------+---------------------+-----------------------+
|              |              |       overhead (usec)        |   bandwidth (MB/s)  |  message rate (msg/s) |
+--------------+--------------+----------+---------+---------+----------+----------+-----------+-----------+
|    Stage     | # iterations | 50.0%ile | average | overall |  average |  overall |  average  |  overall  |
+--------------+--------------+----------+---------+---------+----------+----------+-----------+-----------+
+----------------------------------------------------------------------------------------------------------+
| API:          protocol layer                                                                             |
| Test:         tag match bandwidth                                                                        |
| Data layout:  (automatic)                                                                                |
| Send memory:  rocm                                                                                       |
| Recv memory:  rocm                                                                                       |
| Message size: 100000000                                                                                  |
| Window size:  32                                                                                         |
+----------------------------------------------------------------------------------------------------------+
Final:                    10      7.226   194.001   194.001   491581.66  491581.66        5155        5155
