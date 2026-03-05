Remote Key
==========

.. role:: py(code)
   :language: c++
   :class: highlight

The ``ucxx::RemoteKey`` class wraps a UCP remote key (``ucp_rkey_h``). Remote keys are
used in RMA operations to access memory on a remote process. They are obtained by
packing a memory handle on the remote side and unpacking it locally.

``#include <ucxx/remote_key.h>``

namespace *ucxx*

.. doxygenclass:: ucxx::RemoteKey
    :project: UCXX
    :members:

Factory Functions
-----------------

``#include <ucxx/constructors.h>``

.. doxygenfunction:: ucxx::createRemoteKeyFromMemoryHandle
    :project: UCXX

.. doxygenfunction:: ucxx::createRemoteKeyFromSerialized
    :project: UCXX
