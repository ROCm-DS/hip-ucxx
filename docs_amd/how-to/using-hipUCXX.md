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
