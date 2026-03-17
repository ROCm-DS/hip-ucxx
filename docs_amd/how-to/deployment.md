<!-- SPDX-FileCopyrightText: Copyright (c) 2026 Advanced Micro Devices, Inc. -->
<!-- SPDX-License-Identifier: MIT -->

# ROCm-IPC and Docker/Kubernetes

In order to use ROCm-IPC when running in containers using Docker and/or
Kubernetes the processes must share an IPC namespace for ROCm-IPC to work
correctly.

## Many GPUs in one container

The simplest way to ensure that processes accessing GPUs share an IPC
namespace is to run the processes within the same container. This means
exposing multiple GPUs to a single container.

To expose AMD GPUs to a Docker container, use the `--device` flag:

```bash
docker run --device=/dev/kfd --device=/dev/dri --group-add video <image>
```

## Many containers with a shared IPC namespace

If you wish to isolate your processes into multiple containers and
expose one or more GPUs to each container you need to ensure they are
using a shared IPC namespace.

In a Docker configuration you can mark one container as having a
shareable IPC namespace with the flag `--ipc="shareable"`. Other
containers can then share that namespace with the flag
`--ipc="container:<name-or-ID>"` and passing the name or ID of the
container that is sharing its namespace.

You can also share the host IPC namespace with your container with the
flag `--ipc="host"`, however this is not recommended on multi-tenant
hosts.

Privileged pods in a Kubernetes cluster [can also be configured to share
the host IPC](https://kubernetes.io/docs/concepts/policy/pod-security-policy/#host-namespaces).

For Kubernetes, the [AMD GPU device plugin](https://github.com/ROCm/k8s-device-plugin)
can be used to expose AMD GPUs to pods.

For more information see the [Docker documentation](https://docs.docker.com/engine/reference/run/#ipc-settings---ipc)
and the [ROCm Docker documentation](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/how-to/docker.html).
