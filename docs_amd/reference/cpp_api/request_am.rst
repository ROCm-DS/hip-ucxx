Active Message Request
======================

.. role:: py(code)
   :language: c++
   :class: highlight

The ``ucxx::RequestAm`` class implements non-blocking active message (AM) send and
receive operations. Active messages allow user-defined callbacks to be invoked on the
receiver side when a message arrives, enabling RPC-style communication patterns.

``#include <ucxx/request_am.h>``

namespace *ucxx*

.. doxygenclass:: ucxx::RequestAm
    :project: UCXX
    :members:

Factory Functions
-----------------

``#include <ucxx/constructors.h>``

.. doxygenfunction:: ucxx::createRequestAm
    :project: UCXX
