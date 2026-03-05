# SPDX-FileCopyrightText: Copyright (c) 2026 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: MIT

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

version_number = "0.1.0"  # TODO: Parse this from a centralized location.
left_nav_title = f"hipUCXX {version_number} documentation"

# for PDF output on Read the Docs
project = "hipUCXX"
author = "Advanced Micro Devices, Inc."
copyright = "Copyright (c) 2026 Advanced Micro Devices, Inc. All rights reserved."
version = version_number
release = version_number
cpp_maximum_signature_line_length = 10
setting_all_article_info = True
all_article_info_os = ["linux"]
all_article_info_author = ""

external_projects_current_project = "hipUCXX"

html_context = {
    "docs_header_version": "26.03"
}
html_theme = "rocm_docs_theme"
html_theme_options = {
    "flavor": "rocm-ds",
    "repository_url": "https://github.com/AMD-AIOSS/hipUCXX/"
}

external_toc_path = "./sphinx/_toc.yml"
doxygen_root = "doxygen"
doxysphinx_enabled = True
doxygen_project = {
    "name": "doxygen",
    "path": "doxygen/xml",
}

extensions = [
    "rocm_docs",
    "rocm_docs.doxygen",
    "breathe",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.napoleon",
    "sphinx_copybutton",
    "autoapi.extension"
]

myst_heading_anchors = 4
autosectionlabel_prefix_document = True
napoleon_preprocess_types = True
autodoc_typehints = "description"

# Breathe configuration for Doxygen
breathe_projects = {"UCXX": "./doxygen/xml"}
breathe_default_project = "UCXX"

autoapi_type = "python"
autoapi_dirs = ["./reference/ucxx_api/stubs"]
autoapi_file_patterns = ["*.pyi"]
autoapi_add_toctree_entry = False
autoapi_generate_api_docs = False

suppress_warnings = [
    "etoc.toctree",
]

source_suffix = {
    ".rst": "restructuredtext",
}
