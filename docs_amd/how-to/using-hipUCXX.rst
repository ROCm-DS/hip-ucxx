.. meta::
  :description: hip-ucxx documentation and API reference library
  :keywords: UCX, UCXX, communication, networking, GPU-direct, RDMA, ROCm, ROCm-DS, AMD, HIP

.. _using-ucxx:

**************
Using hip-ucxx
**************

Example code demonstrating the use of the hip-ucxx library is provided in the repository, and in
the following text. Both C++ and Python examples are available. These examples can be used as
templates for building your own application with hip-ucxx, or for adding it to existing projects.

C++ examples
============

The C++ examples are located in `cpp/examples <https://github.com/ROCm-DS/hip-ucxx/tree/release/rocmds-26.03/cpp/examples>`_.
See :ref:`building-ucxx` for instructions on setting up your developer environment.

To build the C++ examples, use the provided ``build.hip.sh`` script:

.. code-block:: bash

   ./build.hip.sh libucxx libucxx-ex

Basic client/server example
---------------------------

The ``basic`` example demonstrates the core hip-ucxx workflow: creating a context,
worker, listener, and endpoint, then performing tag-based send/receive operations.
This example runs both a server and a client within the same process.

The key steps in the example are:

1. Create a ``ucxx::Context`` with default feature flags (tag, stream, AM, RMA, wakeup).
2. Create a ``ucxx::Worker`` from the context.
3. Set up a ``ucxx::Listener`` on the server side to accept incoming connections.
4. Create a client ``ucxx::Endpoint`` by connecting to the listener's address.
5. Use ``tagSend()`` and ``tagRecv()`` on the endpoints to exchange data.
6. Wait for all requests to complete using the worker's progress mechanism.

Running the example
-------------------

.. code-block:: bash

   ./cpp/build/examples/basic -P blocking

Output:

.. code-block:: text

   Server received a connection request from client at address 127.0.0.1:xxxxx
   Example completed successfully

Code walkthrough
----------------

The setup phase creates the fundamental UCXX objects:

.. code-block:: cpp

   #include <ucxx/api.h>

   auto context = ucxx::createContext({}, ucxx::Context::defaultFeatureFlags);
   auto worker  = context->createWorker();
   auto listener = worker->createListener(port, listener_cb, listener_ctx.get());
   auto endpoint = worker->createEndpointFromHostname("127.0.0.1", port, true);

Tag-based communication uses ``tagSend()`` and ``tagRecv()``:

.. code-block:: cpp

   auto send_request = endpoint->tagSend(data, size, ucxx::Tag{0});
   auto recv_request = endpoint->tagRecv(buffer, size, ucxx::Tag{0}, ucxx::TagMaskFull);

   while (!send_request->isCompleted())
       worker->progress();
   send_request->checkError();

Linking against hip-ucxx in CMake
--------------------------------

To use hip-ucxx in your own CMake project:

.. code-block:: cmake

   find_package(ucxx REQUIRED)
   target_link_libraries(your_target PRIVATE ucxx::ucxx)

Python examples
===============

The Python API provides both a low-level interface (via ``ucxx.core``) and an
async-friendly interface (via ``ucxx._lib_async``).

Basic Python usage
------------------

The ``ucxx.core`` module provides functions to initialize UCX, create listeners,
and establish communication:

.. code-block:: python

   import ucxx

   # Initialize UCX
   ucxx.init()

   # Get UCX version information
   version = ucxx.get_ucx_version()
   print(f"UCX version: {version}")

   # Create a listener
   async def handler(endpoint):
       data = await endpoint.recv()
       print(f"Received: {data}")

   listener = ucxx.create_listener(handler, port=12345)
   print(f"Listening on port {listener.port}")

Async communication with ApplicationContext
-------------------------------------------

For more advanced usage, the ``ApplicationContext`` provides a higher-level
async API:

.. code-block:: python

   import asyncio
   from ucxx._lib_async import ApplicationContext

   async def main():
       ctx = ApplicationContext()

       # Server side
       async def server_handler(ep):
           data = bytearray(b"Hello from server!")
           await ep.send(data)

       listener = ctx.create_listener(server_handler, port=0)
       port = listener.port

       # Client side
       ep = await ctx.create_endpoint("127.0.0.1", port)
       msg = bytearray(18)
       await ep.recv(msg)
       print(f"Client received: {msg.decode()}")

   asyncio.run(main())

Python basic example
--------------------

The repository includes a comprehensive low-level example at
``python/ucxx/examples/basic.py`` that demonstrates the ``ucx_api`` interface
directly. This example covers context/worker/listener/endpoint creation,
tag-based transfers, and configurable progress modes.

To run the example:

.. code-block:: bash

   python python/ucxx/examples/basic.py --progress-mode blocking
   python python/ucxx/examples/basic.py --progress-mode thread
   python python/ucxx/examples/basic.py --multi-buffer-transfer

Key options:

- ``--progress-mode`` (``thread`` or ``blocking``) -- controls how UCX progress is driven
- ``--object-type`` (``numpy`` or ``rmm``) -- selects the buffer type for transfers
- ``--multi-buffer-transfer`` -- enables multi-buffer transfer mode

For additional Python examples, see the ``python/ucxx/ucxx/examples/`` directory
in the repository.

Multi-process server/client example
-----------------------------------

The examples above run the server and client within the same process. The
following demonstrates a more realistic multi-process pattern where the server
and client run in separate terminals.

Send/Receive NumPy arrays
-------------------------

**Process 1 -- Server** (run in one terminal):

.. code-block:: python

   import asyncio
   import ucxx
   import numpy as np

   n_bytes = 2**30
   host = ucxx.get_address()  # specify interface with ifname="..." if needed
   port = 13337


   async def send(ep):
       arr = np.empty(n_bytes, dtype="u1")
       await ep.recv(arr)
       assert np.count_nonzero(arr) == np.array(0, dtype=np.int64)
       print("Received NumPy array")

       arr += 1
       print("Sending incremented NumPy array")
       await ep.send(arr)

       lf.close()


   async def main():
       global lf
       lf = ucxx.create_listener(send, port)

       while not lf.closed:
           await asyncio.sleep(0.1)

   if __name__ == "__main__":
       asyncio.run(main())

**Process 2 -- Client** (run in a second terminal):

.. code-block:: python

   import asyncio
   import ucxx
   import numpy as np

   port = 13337
   n_bytes = 2**30


   async def main():
       host = ucxx.get_address()  # specify interface with ifname="..." if needed
       ep = await ucxx.create_endpoint(host, port)
       msg = np.zeros(n_bytes, dtype="u1")

       print("Send Original NumPy array")
       await ep.send(msg)

       print("Receive Incremented NumPy array")
       resp = np.empty_like(msg)
       await ep.recv(resp)
       np.testing.assert_array_equal(msg + 1, resp)


   if __name__ == "__main__":
       asyncio.run(main())

Send/Recv amd-cupy arrays
-------------------------

.. note::
   If you are passing amd-cupy arrays between GPUs and want to use
   ROCm-IPC for GPU-to-GPU
   transfers, ensure you have correctly set ``UCX_TLS`` to include
   ``rocm_ipc``. For example: ``UCX_TLS=tcp,rocm_ipc,rocm_copy``.

**Process 1 -- Server** (run in one terminal):

.. code-block:: python

   import asyncio
   import ucxx
   import cupy as cp

   n_bytes = 2**30
   host = ucxx.get_address()  # specify interface with ifname="..." if needed
   port = 13337


   async def send(ep):
       arr = cp.empty(n_bytes, dtype="u1")
       await ep.recv(arr)
       assert cp.count_nonzero(arr) == cp.array(0, dtype=cp.int64)
       print("Received amd-cupy array")

       arr += 1
       print("Sending incremented amd-cupy array")
       await ep.send(arr)

       lf.close()


   async def main():
       global lf
       lf = ucxx.create_listener(send, port)

       while not lf.closed:
           await asyncio.sleep(0.1)


   if __name__ == "__main__":
       asyncio.run(main())

**Process 2 -- Client** (run in a second terminal):

.. code-block:: python

   import asyncio
   import ucxx
   import cupy as cp

   port = 13337
   n_bytes = 2**30


   async def main():
       host = ucxx.get_address()  # specify interface with ifname="..." if needed
       ep = await ucxx.create_endpoint(host, port)
       msg = cp.zeros(n_bytes, dtype="u1")

       print("Send Original amd-cupy array")
       await ep.send(msg)

       print("Receive Incremented amd-cupy array")
       resp = cp.empty_like(msg)
       await ep.recv(resp)
       cp.testing.assert_array_equal(msg + 1, resp)

   if __name__ == "__main__":
       asyncio.run(main())
