Future
======

.. role:: py(code)
   :language: c++
   :class: highlight

The ``ucxx::Future`` class provides a future-based mechanism for tracking the completion
of asynchronous UCXX operations. Futures can be used to bridge UCXX requests with
external event loops (e.g., Python asyncio).

``#include <ucxx/future.h>``

namespace *ucxx*

.. doxygenclass:: ucxx::Future
    :project: UCXX
    :members:
