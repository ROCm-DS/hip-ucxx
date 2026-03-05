Utilities
=========

.. role:: py(code)
   :language: c++
   :class: highlight

This page provides references for utility types and functions in the ``ucxx`` library,
including type definitions, multi-buffer header metadata, exception handling, and
miscellaneous helpers.

Type Definitions
----------------

``#include <ucxx/typedefs.h>``

namespace *ucxx*

.. doxygenfile:: ucxx/typedefs.h
    :project: UCXX

Header
------

The ``ucxx::Header`` class provides metadata for multi-buffer transfers, describing
the layout and types of buffers being transferred.

``#include <ucxx/header.h>``

namespace *ucxx*

.. doxygenclass:: ucxx::Header
    :project: UCXX
    :members:

Exceptions
----------

``#include <ucxx/exception.h>``

namespace *ucxx*

.. doxygenfile:: ucxx/exception.h
    :project: UCXX

Utility Helpers
---------------

Socket Address Utilities
~~~~~~~~~~~~~~~~~~~~~~~~

``#include <ucxx/utils/sockaddr.h>``

namespace *ucxx::utils*

.. doxygenfile:: ucxx/utils/sockaddr.h
    :project: UCXX

File Descriptor Utilities
~~~~~~~~~~~~~~~~~~~~~~~~~

``#include <ucxx/utils/file_descriptor.h>``

namespace *ucxx::utils*

.. doxygenfile:: ucxx/utils/file_descriptor.h
    :project: UCXX

UCX Wrappers
~~~~~~~~~~~~

``#include <ucxx/utils/ucx.h>``

namespace *ucxx::utils*

.. doxygenfile:: ucxx/utils/ucx.h
    :project: UCXX
