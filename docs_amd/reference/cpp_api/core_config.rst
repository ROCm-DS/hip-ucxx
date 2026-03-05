Config
======

.. role:: py(code)
   :language: c++
   :class: highlight

The ``ucxx::Config`` class provides access to UCX configuration parameters. It wraps
the UCP configuration and allows querying and setting ``UCX_*`` environment variable
overrides used during context creation.

``#include <ucxx/config.h>``

namespace *ucxx*

.. doxygenclass:: ucxx::Config
    :project: UCXX
    :members:
