# SPDX-FileCopyrightText: Copyright (c) 2023-2025, NVIDIA CORPORATION & AFFILIATES.
# SPDX-FileCopyrightText: Copyright (c) 2026 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: BSD-3-Clause AND MIT

from .ucxx import (
    UCXXBackend,
    UCXXBackendLegacyPrefix,
)  # noqa: F401


from ._version import __git_commit__, __version__

try:
    import numba.hip

    numba.hip.pose_as_cuda()
except ModuleNotFoundError:
    pass
