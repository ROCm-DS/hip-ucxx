Worker
======

.. role:: py(code)
   :language: c++
   :class: highlight

The ``ucxx::Worker`` class encapsulates a UCP worker (``ucp_worker_h``). Workers are the
primary communication objects that manage endpoints, listeners, and progress operations.
Workers are created from a ``ucxx::Context`` via ``context->createWorker()``.

``#include <ucxx/worker.h>``

namespace *ucxx*

.. doxygenclass:: ucxx::Worker
    :project: UCXX
    :members:

Worker Progress Thread
----------------------

``#include <ucxx/worker_progress_thread.h>``

namespace *ucxx*

.. doxygenclass:: ucxx::WorkerProgressThread
    :project: UCXX
    :members:
