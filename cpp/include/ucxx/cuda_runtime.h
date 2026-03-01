/**
 * SPDX-FileCopyrightText: Copyright (c) 2026 Advanced Micro Devices, Inc.
 * SPDX-License-Identifier: MIT
 */
#pragma once

#include <hip/hip_runtime.h>

// types
#ifndef cudaError_t
#define cudaError_t hipError_t
#endif
#ifndef cudaStream_t
#define cudaStream_t hipStream_t
#endif

// macros, enum constant definitions
#ifndef cudaMemcpyDefault
#define cudaMemcpyDefault hipMemcpyDefault
#endif
#ifndef cudaMemcpyDeviceToDevice
#define cudaMemcpyDeviceToDevice hipMemcpyDeviceToDevice
#endif
#ifndef cudaMemcpyDeviceToHost
#define cudaMemcpyDeviceToHost hipMemcpyDeviceToHost
#endif
#ifndef cudaMemcpyHostToDevice
#define cudaMemcpyHostToDevice hipMemcpyHostToDevice
#endif
#ifndef cudaSuccess
#define cudaSuccess hipSuccess
#endif

// functions
#ifndef cudaFree
#define cudaFree hipFree
#endif
#ifndef cudaFreeAsync
#define cudaFreeAsync hipFreeAsync
#endif
#ifndef cudaGetErrorString
#define cudaGetErrorString hipGetErrorString
#endif
#ifndef cudaMalloc
#define cudaMalloc hipMalloc
#endif
#ifndef cudaMallocAsync
#define cudaMallocAsync hipMallocAsync
#endif
#ifndef cudaMallocManaged
#define cudaMallocManaged hipMallocManaged
#endif
#ifndef cudaMemcpy
#define cudaMemcpy hipMemcpy
#endif
#ifndef cudaMemcpyAsync
#define cudaMemcpyAsync hipMemcpyAsync
#endif
#ifndef cudaSetDevice
#define cudaSetDevice hipSetDevice
#endif
#ifndef cudaStreamCreate
#define cudaStreamCreate hipStreamCreate
#endif
#ifndef cudaStreamDestroy
#define cudaStreamDestroy hipStreamDestroy
#endif
#ifndef cudaStreamSynchronize
#define cudaStreamSynchronize hipStreamSynchronize
#endif
