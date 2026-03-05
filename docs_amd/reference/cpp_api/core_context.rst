Context
=======

.. role:: py(code)
   :language: c++
   :class: highlight

The ``ucxx::Context`` class encapsulates a UCP context (``ucp_context_h``). It is the
top-level object in the UCXX hierarchy and must be created before any other UCXX objects.
Contexts are created via the ``ucxx::createContext()`` factory function.

``#include <ucxx/context.h>``

namespace *ucxx*

.. doxygenclass:: ucxx::Context
    :project: UCXX
    :members:

Factory Functions
-----------------

``#include <ucxx/constructors.h>``

.. doxygenfunction:: ucxx::createContext
    :project: UCXX
