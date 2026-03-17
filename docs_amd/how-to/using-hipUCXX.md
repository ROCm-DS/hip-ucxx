<!-- SPDX-FileCopyrightText: Copyright (c) 2026 Advanced Micro Devices, Inc. -->
<!-- SPDX-License-Identifier: MIT -->

# Using hipUCXX

Example code demonstrating the use of the hipUCXX library is provided
in the repository. Both C++ and Python examples are available. These
examples can be used as templates to build your own application using
hipUCXX or to add hipUCXX to existing projects.

# C++ examples

To build the C++ examples, use the provided `build.hip.sh` script:

```bash
./build.hip.sh libucxx libucxx-ex
```

The C++ examples are located in `cpp/examples/`. Refer to the
[Building hipUCXX from source](../install/build.md#building-hipucxx-from-source) documentation
for instructions on how to set up your developer environment.

## Basic client/server example

The `basic` example demonstrates the core hipUCXX workflow: creating a context,
worker, listener, and endpoint, then performing tag-based send/receive operations.
This example runs both a server and a client within the same process.

The key steps in the example are:

1. Create a `ucxx::Context` with default feature flags (tag, stream, AM, RMA, wakeup).
2. Create a `ucxx::Worker` from the context.
3. Set up a `ucxx::Listener` on the server side to accept incoming connections.
4. Create a client `ucxx::Endpoint` by connecting to the listener's address.
5. Use `tagSend()` and `tagRecv()` on the endpoints to exchange data.
6. Wait for all requests to complete using the worker's progress mechanism.

### Running the example

```bash
./cpp/build/examples/basic -P blocking
```

Output:
```
Server received a connection request from client at address 127.0.0.1:xxxxx
Example completed successfully
```

### Code walkthrough

The setup phase creates the fundamental UCXX objects:

```cpp
#include <ucxx/api.h>

auto context = ucxx::createContext({}, ucxx::Context::defaultFeatureFlags);
auto worker  = context->createWorker();
auto listener = worker->createListener(port, listener_cb, listener_ctx.get());
auto endpoint = worker->createEndpointFromHostname("127.0.0.1", port, true);
```

Tag-based communication uses `tagSend()` and `tagRecv()`:

```cpp
auto send_request = endpoint->tagSend(data, size, ucxx::Tag{0});
auto recv_request = endpoint->tagRecv(buffer, size, ucxx::Tag{0}, ucxx::TagMaskFull);

while (!send_request->isCompleted())
    worker->progress();
send_request->checkError();
```

### Linking against hipUCXX in CMake

To use hipUCXX in your own CMake project:

```cmake
find_package(ucxx REQUIRED)
target_link_libraries(your_target PRIVATE ucxx::ucxx)
```

# Python examples

The Python API provides both a low-level interface (via `ucxx.core`) and an
async-friendly interface (via `ucxx._lib_async`).

## Basic Python usage

The `ucxx.core` module provides functions to initialize UCX, create listeners,
and establish communication:

```python
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
```

## Async communication with ApplicationContext

For more advanced usage, the `ApplicationContext` provides a higher-level
async API:

```python
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
```

For additional Python examples, see the `python/ucxx/ucxx/examples/` directory
in the repository.

## Multi-process server/client example

The examples above run server and client within the same process. The
following demonstrates a more realistic multi-process pattern where server
and client run in separate terminals.

### Send/Recv NumPy arrays

**Process 1 -- Server** (run in one terminal):

```python
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
```

**Process 2 -- Client** (run in a second terminal):

```python
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
```

### Send/Recv amd-cupy arrays

```{note}
If you are passing amd-cupy arrays between GPUs and want to use
[ROCm-IPC](https://rocm.docs.amd.com/en/latest/) for GPU-to-GPU
transfers, ensure you have correctly set `UCX_TLS` to include
`rocm_ipc`. See the [Configuration](configuration.md) page for details.
```

**Process 1 -- Server** (run in one terminal):

```python
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
```

**Process 2 -- Client** (run in a second terminal):

```python
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
```
