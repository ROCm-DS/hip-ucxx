Listener
========

.. role:: py(code)
   :language: c++
   :class: highlight

The ``ucxx::Listener`` class encapsulates a UCP listener (``ucp_listener_h``). Listeners
bind to a port and accept incoming connection requests from remote endpoints.
A user-defined callback is invoked when a new connection is received.

``#include <ucxx/listener.h>``

namespace *ucxx*

.. doxygenclass:: ucxx::Listener
    :project: UCXX
    :members:

Factory Functions
-----------------

``#include <ucxx/constructors.h>``

.. doxygenfunction:: ucxx::createListener
    :project: UCXX
