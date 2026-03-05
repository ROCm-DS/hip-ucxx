#!/bin/bash
# SPDX-FileCopyrightText: Copyright (c) 2026 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: MIT
#
# Generate Python .pyi stub files for sphinx-autoapi documentation.
# Requires a working installation of amd-hipucxx (ROCm + UCX).

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

pip install pybind11-stubgen

echo "Generating stubs..."
pybind11-stubgen --ignore-all-errors ucxx
pybind11-stubgen --ignore-all-errors ucxx.core
pybind11-stubgen --ignore-all-errors ucxx._lib_async
pybind11-stubgen --ignore-all-errors ucxx._lib.libucxx
pybind11-stubgen --ignore-all-errors ucxx._lib.arr
pybind11-stubgen --ignore-all-errors ucxx.types
pybind11-stubgen --ignore-all-errors ucxx.exceptions
pybind11-stubgen --ignore-all-errors ucxx.utils

# Replace generated stubs with symlinks to hand-maintained overrides.
# The overrides use inline class definitions for exception types that are
# dynamically created by _create_exceptions() in Cython, which pybind11-stubgen
# generates as unresolvable "from ucxx import UCXXError" imports.
echo "Applying overrides..."
rm -f stubs/ucxx/exceptions.pyi
ln -sv ../../overrides/ucxx/exceptions.pyi stubs/ucxx/exceptions.pyi

rm -f stubs/ucxx/__init__.pyi
ln -sv ../../overrides/ucxx/__init__.pyi stubs/ucxx/__init__.pyi

rm -f stubs/ucxx/_lib/libucxx.pyi
ln -sv ../../../overrides/ucxx/_lib/libucxx.pyi stubs/ucxx/_lib/libucxx.pyi

echo "Done. Stubs are in stubs/ with overrides symlinked."
