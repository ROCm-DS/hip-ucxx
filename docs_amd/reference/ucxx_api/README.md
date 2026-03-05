<!-- SPDX-FileCopyrightText: Copyright (c) 2026 Advanced Micro Devices, Inc. -->
<!-- SPDX-License-Identifier: MIT -->

# Generating the stubs

In order to generate the Python API documentation from an environment where `amd-hipucxx` is unavailable, `.pyi` stub files must be generated. These stubs provide type information that `sphinx-autoapi` uses to render the Python API reference pages.

## Prerequisites

- A working installation of `amd-hipucxx` (requires ROCm and UCX)
- The `pybind11-stubgen` package

## Generating stubs

From an environment with `amd-hipucxx` installed, run:

```bash
cd <UCXX_ROOT>/docs_amd/reference/ucxx_api
./generate_stubs.sh
```

The script runs `pybind11-stubgen` for all relevant modules and then replaces
certain generated stubs with symlinks to hand-maintained versions in the
`overrides/` directory.

## Overrides directory

The `overrides/` directory contains hand-maintained `.pyi` stubs for modules
where `pybind11-stubgen` generates unresolvable imports. Specifically, the
UCXX exception classes (e.g., `UCXError`, `UCXCanceledError`) are dynamically
created by `_create_exceptions()` in Cython, causing `pybind11-stubgen` to
emit `from ucxx import UCXXError` imports that `sphinx-autoapi` cannot resolve.
The override files replace these with inline class definitions.

The generated stubs will be placed in the `stubs/` directory. These stubs are checked
into the repository, so this step should only be necessary if the API has changed.

The stubs are then used by the `autoapi.extension` (configured in `conf.py`) to generate
the API documentation pages.
