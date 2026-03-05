Delayed Submission
==================

.. role:: py(code)
   :language: c++
   :class: highlight

The delayed submission module provides a mechanism to defer the submission of UCXX
requests to the worker progress thread, rather than submitting them immediately from
the calling thread. This is useful for thread-safety when multiple threads submit
requests concurrently.

``#include <ucxx/delayed_submission.h>``

namespace *ucxx*

.. doxygenfile:: ucxx/delayed_submission.h
    :project: UCXX

Inflight Requests
-----------------

``#include <ucxx/inflight_requests.h>``

namespace *ucxx*

.. doxygenclass:: ucxx::InflightRequests
    :project: UCXX
    :members:
