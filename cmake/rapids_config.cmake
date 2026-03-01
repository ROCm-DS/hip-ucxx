# =============================================================================
# Copyright (c) 2018-2025, NVIDIA CORPORATION.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations under
# the License.
# =============================================================================
# SPDX-FileCopyrightText: Copyright (c) 2026 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: Apache-2.0 AND MIT
# =============================================================================

file(READ "${CMAKE_CURRENT_LIST_DIR}/../ROCmDS_VERSION" _rocmds_version)
if(_rocmds_version MATCHES [[^([0-9][0-9])\.([0-9][0-9])\.([0-9][0-9])]])
  set(ROCmDS_VERSION_MAJOR "${CMAKE_MATCH_1}")
  set(ROCmDS_VERSION_MINOR "${CMAKE_MATCH_2}")
  set(ROCmDS_VERSION_PATCH "${CMAKE_MATCH_3}")
  set(ROCmDS_VERSION_MAJOR_MINOR "${ROCmDS_VERSION_MAJOR}.${ROCmDS_VERSION_MINOR}")
  set(ROCmDS_VERSION "${ROCmDS_VERSION_MAJOR}.${ROCmDS_VERSION_MINOR}.${ROCmDS_VERSION_PATCH}")
else()
  string(REPLACE "\n" "\n  " _rocmds_version_formatted "  ${_rocmds_version}")
  message(
    FATAL_ERROR
      "Could not determine ROCmDS version. Contents of ROCmDS_VERSION file:\n${_rocmds_version_formatted}"
  )
endif()

set(rapids-cmake-version "${ROCmDS_VERSION_MAJOR_MINOR}")
include("${CMAKE_CURRENT_LIST_DIR}/RAPIDS.cmake")
