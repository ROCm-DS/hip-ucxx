Component
=========

.. role:: py(code)
   :language: c++
   :class: highlight

The ``ucxx::Component`` class is the base class for all UCXX objects that participate in
the ownership hierarchy. It provides parent-child relationship management to ensure correct
lifetime ordering of UCXX objects.

``#include <ucxx/component.h>``

namespace *ucxx*

.. doxygenclass:: ucxx::Component
    :project: UCXX
    :members:
