Tag Request
===========

.. role:: py(code)
   :language: c++
   :class: highlight

The ``ucxx::RequestTag`` class implements non-blocking tag-based send and receive
operations using the UCX Tag API (``ucp_tag_send_nbx`` / ``ucp_tag_recv_nbx``).
Tags allow sender-receiver matching based on a user-specified tag value.

``#include <ucxx/request_tag.h>``

namespace *ucxx*

.. doxygenclass:: ucxx::RequestTag
    :project: UCXX
    :members:

Factory Functions
-----------------

``#include <ucxx/constructors.h>``

.. doxygenfunction:: ucxx::createRequestTag
    :project: UCXX
