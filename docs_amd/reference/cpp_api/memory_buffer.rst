Buffer
======

.. role:: py(code)
   :language: c++
   :class: highlight

The buffer classes provide abstractions over raw memory pointers. ``ucxx::Buffer`` is the
abstract base class, with ``ucxx::HostBuffer`` for host memory and ``ucxx::RMMBuffer`` for
GPU device memory managed by hipMM (which preserves the upstream ``rmm`` namespace).

``#include <ucxx/buffer.h>``

namespace *ucxx*

.. doxygenenum:: ucxx::BufferType
    :project: UCXX

.. doxygenclass:: ucxx::Buffer
    :project: UCXX
    :members:

.. doxygenclass:: ucxx::HostBuffer
    :project: UCXX
    :members:

.. doxygenclass:: ucxx::RMMBuffer
    :project: UCXX
    :members:
