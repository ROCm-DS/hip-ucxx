Core
====

This page provides ``ucxx`` class and function references for the publicly-exposed elements of the ``ucxx.core`` module. This module provides the primary interface for initializing UCX, creating listeners and endpoints, and managing the communication lifecycle.

.. role:: py(code)
   :language: python
   :class: highlight

Initialization and Configuration
#################################

.. autoapifunction:: ucxx.core.init

.. autoapifunction:: ucxx.core.reset

.. autoapifunction:: ucxx.core.get_config

.. autoapifunction:: ucxx.core.get_ucx_version

Communication
#############

.. autoapifunction:: ucxx.core.create_listener

.. autoapifunction:: ucxx.core.progress

.. autoapifunction:: ucxx.core.continuous_ucx_progress

Worker and Context Information
##############################

.. autoapifunction:: ucxx.core.get_ucp_context_info

.. autoapifunction:: ucxx.core.get_ucp_worker_info

.. autoapifunction:: ucxx.core.get_active_transports

.. autoapifunction:: ucxx.core.get_worker_address

.. autoapifunction:: ucxx.core.get_ucp_worker

.. autoapifunction:: ucxx.core.get_ucxx_worker

.. autoapifunction:: ucxx.core.get_ucx_address_from_buffer

Thread Management
#################

.. autoapifunction:: ucxx.core.stop_notifier_thread
