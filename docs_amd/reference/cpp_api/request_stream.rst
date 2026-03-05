Stream Request
==============

.. role:: py(code)
   :language: c++
   :class: highlight

The ``ucxx::RequestStream`` class implements non-blocking stream-based send and
receive operations using the UCX Stream API. Stream communication provides
ordered, byte-stream semantics over an endpoint.

``#include <ucxx/request_stream.h>``

namespace *ucxx*

.. doxygenclass:: ucxx::RequestStream
    :project: UCXX
    :members:

Factory Functions
-----------------

``#include <ucxx/constructors.h>``

.. doxygenfunction:: ucxx::createRequestStream
    :project: UCXX
