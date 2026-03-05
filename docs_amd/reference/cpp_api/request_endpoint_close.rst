Endpoint Close Request
======================

.. role:: py(code)
   :language: c++
   :class: highlight

The ``ucxx::RequestEndpointClose`` class implements a non-blocking endpoint close
operation. Closing an endpoint gracefully terminates the connection and releases
associated resources.

``#include <ucxx/request_endpoint_close.h>``

namespace *ucxx*

.. doxygenclass:: ucxx::RequestEndpointClose
    :project: UCXX
    :members:

Factory Functions
-----------------

``#include <ucxx/constructors.h>``

.. doxygenfunction:: ucxx::createRequestEndpointClose
    :project: UCXX
