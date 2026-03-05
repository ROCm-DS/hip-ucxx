Request
=======

This page provides C++ class references for the request types in the ``ucxx`` library.
Requests represent non-blocking communication operations. Each request type corresponds
to a different UCX communication pattern: tag, stream, active message, remote memory
access, flush, and endpoint close.

.. role:: py(code)
   :language: c++
   :class: highlight

Base Request
------------

``#include <ucxx/request.h>``

namespace *ucxx*

.. doxygenclass:: ucxx::Request
    :project: UCXX
    :members:

Request Data
------------

``#include <ucxx/request_data.h>``

namespace *ucxx*

.. doxygenfile:: ucxx/request_data.h
    :project: UCXX

.. toctree::
   :maxdepth: 2
   :caption: Request Types:

   request_tag.rst
   request_tag_multi.rst
   request_stream.rst
   request_am.rst
   request_mem.rst
   request_flush.rst
   request_endpoint_close.rst
