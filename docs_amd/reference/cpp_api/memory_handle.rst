Memory Handle
=============

.. role:: py(code)
   :language: c++
   :class: highlight

The ``ucxx::MemoryHandle`` class wraps a UCP memory handle (``ucp_mem_h``). Memory handles
are used to register memory regions for remote memory access (RMA) operations. A memory
handle can either allocate new memory or map an existing buffer for RMA.

``#include <ucxx/memory_handle.h>``

namespace *ucxx*

.. doxygenclass:: ucxx::MemoryHandle
    :project: UCXX
    :members:

Factory Functions
-----------------

``#include <ucxx/constructors.h>``

.. doxygenfunction:: ucxx::createMemoryHandle
    :project: UCXX
