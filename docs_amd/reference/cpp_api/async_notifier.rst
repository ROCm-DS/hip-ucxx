Notifier
========

.. role:: py(code)
   :language: c++
   :class: highlight

The ``ucxx::Notifier`` class provides a mechanism for notifying external components
when UCXX requests complete. It is used by the worker progress thread to signal
request completion to consumers such as the Python event loop.

``#include <ucxx/notifier.h>``

namespace *ucxx*

.. doxygenclass:: ucxx::Notifier
    :project: UCXX
    :members:
