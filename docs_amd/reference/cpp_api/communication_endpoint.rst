Endpoint
========

.. role:: py(code)
   :language: c++
   :class: highlight

The ``ucxx::Endpoint`` class encapsulates a UCP endpoint (``ucp_ep_h``). Endpoints are the
primary interface for sending and receiving data. They support tag-based, stream-based,
active message, and remote memory access (RMA) communication patterns.

Endpoints can be created from a hostname, a worker address, or from an incoming
connection request on a listener.

``#include <ucxx/endpoint.h>``

namespace *ucxx*

.. doxygenclass:: ucxx::Endpoint
    :project: UCXX
    :members:

.. doxygenstruct:: ucxx::EpParamsDeleter
    :project: UCXX
    :members:

Factory Functions
-----------------

``#include <ucxx/constructors.h>``

.. doxygenfunction:: ucxx::createEndpointFromHostname
    :project: UCXX

.. doxygenfunction:: ucxx::createEndpointFromWorkerAddress
    :project: UCXX

.. doxygenfunction:: ucxx::createEndpointFromConnRequest
    :project: UCXX
