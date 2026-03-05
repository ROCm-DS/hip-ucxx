Address
=======

.. role:: py(code)
   :language: c++
   :class: highlight

The ``ucxx::Address`` class represents a worker address that can be used to establish
connections between endpoints. Addresses are obtained from workers and can be serialized
for out-of-band exchange.

``#include <ucxx/address.h>``

namespace *ucxx*

.. doxygenclass:: ucxx::Address
    :project: UCXX
    :members:

Factory Functions
-----------------

``#include <ucxx/constructors.h>``

.. doxygenfunction:: ucxx::createAddressFromWorker
    :project: UCXX

.. doxygenfunction:: ucxx::createAddressFromString
    :project: UCXX
