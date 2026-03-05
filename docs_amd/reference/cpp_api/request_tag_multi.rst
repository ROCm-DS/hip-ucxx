Tag Multi-Buffer Request
========================

.. role:: py(code)
   :language: c++
   :class: highlight

The ``ucxx::RequestTagMulti`` class implements multi-buffer tag-based transfers. It
coordinates sending or receiving multiple buffers as a single logical operation,
using header metadata to describe the buffer layout.

``#include <ucxx/request_tag_multi.h>``

namespace *ucxx*

.. doxygenclass:: ucxx::RequestTagMulti
    :project: UCXX
    :members:

Factory Functions
-----------------

``#include <ucxx/constructors.h>``

.. doxygenfunction:: ucxx::createRequestTagMulti
    :project: UCXX
