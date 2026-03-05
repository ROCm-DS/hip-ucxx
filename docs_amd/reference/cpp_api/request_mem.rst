Remote Memory Access Request
============================

.. role:: py(code)
   :language: c++
   :class: highlight

The ``ucxx::RequestMem`` class implements non-blocking remote memory access (RMA)
operations. RMA allows direct memory read/write operations on a remote process's
memory without involving the remote CPU, using memory handles and remote keys.

``#include <ucxx/request_mem.h>``

namespace *ucxx*

.. doxygenclass:: ucxx::RequestMem
    :project: UCXX
    :members:

Factory Functions
-----------------

``#include <ucxx/constructors.h>``

.. doxygenfunction:: ucxx::createRequestMem
    :project: UCXX
