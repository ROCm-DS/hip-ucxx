<!-- SPDX-FileCopyrightText: Copyright (c) 2026 Advanced Micro Devices, Inc. -->
<!-- SPDX-License-Identifier: MIT -->

# Monitoring transports

Below is a list of commonly used tools and commands to monitor InfiniBand and ROCm-IPC messages.

## InfiniBand

Monitor InfiniBand packet counters -- this number should dramatically increase when there's InfiniBand traffic:

```bash
watch -n 0.1 'cat /sys/class/infiniband/mlx5_*/ports/1/counters/port_xmit_data'
```

## ROCm-IPC / XGMI

Monitor GPU topology and interconnect access:

```bash
rocm-smi --showtopo
```

Monitor GPU utilization across all GPUs:

```bash
rocm-smi --showuse
```

Monitor XGMI link information and data transfer activity:

```bash
rocm-smi --showtoponuma
```

Display GPU memory usage:

```bash
rocm-smi --showmeminfo vram
```

Continuous monitoring of GPU stats:

```bash
watch -n 1 rocm-smi
```
