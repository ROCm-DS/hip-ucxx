from __future__ import annotations
import logging as logging
import os as os
from queue import Queue
import threading as threading
from ucxx import UCXXMessageTruncatedError as UCXMessageTruncatedError
from ucxx._lib.arr import Array
from ucxx._lib import libucxx as ucx_api
from ucxx._lib.libucxx import UCXXTag as Tag
from ucxx._lib_async.continuous_ucx_progress import BlockingMode
from ucxx._lib_async.continuous_ucx_progress import PollingMode
from ucxx._lib_async.continuous_ucx_progress import ThreadMode
from ucxx._lib_async.endpoint import Endpoint
from ucxx._lib_async.exchange_peer_info import exchange_peer_info
from ucxx._lib_async.listener import ActiveClients
from ucxx._lib_async.listener import Listener
from ucxx._lib_async.listener import _listener_handler
from ucxx._lib_async.notifier_thread import _notifierThread
from ucxx._lib_async.utils import get_event_loop
from ucxx._lib_async.utils import hash64bits
import warnings as warnings
import weakref as weakref
__all__: list[str] = ['ActiveClients', 'ApplicationContext', 'Array', 'BlockingMode', 'Endpoint', 'Listener', 'PollingMode', 'ProgressTasks', 'Queue', 'Tag', 'ThreadMode', 'UCXMessageTruncatedError', 'clear_progress_tasks', 'exchange_peer_info', 'get_event_loop', 'hash64bits', 'logger', 'logging', 'os', 'threading', 'ucx_api', 'warnings', 'weakref']
class ApplicationContext:
    """

        The context of the Asyncio interface of UCX.

    """
    _enable_delayed_submission = None
    _enable_python_future = None
    _progress_mode = None
    enable_delayed_submission = ...
    enable_python_future = ...
    progress_mode = ...
    def __init__(self, config_dict = {}, progress_mode = None, enable_delayed_submission = None, enable_python_future = None, connect_timeout = None):
        ...
    def clear_progress_tasks(self) -> None:
        ...
    def continuous_ucx_progress(self, event_loop = None):
        """
        Guarantees continuous UCX progress

                Use this function to associate UCX progress with an event loop.
                Notice, multiple event loops can be associate with UCX progress.

                This function is automatically called when calling
                `create_listener()` or `create_endpoint()`.

                Parameters
                ----------
                event_loop: asyncio.event_loop, optional
                    The event loop to evoke UCX progress. If None,
                    `asyncio.get_event_loop()` (`asyncio.new_event_loop()` in
                    Python 3.10+) is used.

        """
    def create_endpoint(self, ip_address, port, endpoint_error_handling = True, connect_timeout = 5.0):
        """
        Create a new endpoint to a server

                Parameters
                ----------
                ip_address: str
                    IP address of the server the endpoint should connect to
                port: int
                    IP address of the server the endpoint should connect to
                endpoint_error_handling: boolean, optional
                    If `True` (default) enable endpoint error handling raising
                    exceptions when an error occurs, may incur in performance penalties
                    but prevents a process from terminating unexpectedly that may
                    happen when disabled. If `False` endpoint endpoint error handling
                    is disabled.
                connect_timeout: float
                    Timeout in seconds for exchanging peer info. In some cases, exchanging
                    peer information may hang indefinitely, a timeout prevents that. If the
                    chosen value is too high it may cause the operation to be stuck for too
                    long rather than quickly raising a `TimeoutError` that may be recovered
                    from by the application, but under high-load a higher timeout may
                    be helpful to prevent exchanging peer info from failing too fast.

                Returns
                -------
                Endpoint
                    The new endpoint

        """
    def create_endpoint_from_worker_address(self, address, endpoint_error_handling = True):
        """
        Create a new endpoint to a server

                Parameters
                ----------
                address: UCXAddress
                endpoint_error_handling: boolean, optional
                    If `True` (default) enable endpoint error handling raising
                    exceptions when an error occurs, may incur in performance penalties
                    but prevents a process from terminating unexpectedly that may
                    happen when disabled. If `False` endpoint endpoint error handling
                    is disabled.

                Returns
                -------
                Endpoint
                    The new endpoint

        """
    def create_listener(self, callback_func, port = 0, endpoint_error_handling = True, connect_timeout = 5.0):
        """
        Create and start a listener to accept incoming connections

                callback_func is the function or coroutine that takes one
                argument -- the Endpoint connected to the client.

                Notice, the listening is closed when the returned Listener
                goes out of scope thus remember to keep a reference to the object.

                Parameters
                ----------
                callback_func: function or coroutine
                    A callback function that gets invoked when an incoming
                    connection is accepted
                port: int, optional
                    An unused port number for listening, or `0` to let UCX assign
                    an unused port.
                endpoint_error_handling: boolean, optional
                    If `True` (default) enable endpoint error handling raising
                    exceptions when an error occurs, may incur in performance penalties
                    but prevents a process from terminating unexpectedly that may
                    happen when disabled. If `False` endpoint endpoint error handling
                    is disabled.
                connect_timeout: float
                    Timeout in seconds for exchanging peer info. In some cases, exchanging
                    peer information may hang indefinitely, a timeout prevents that. If the
                    chosen value is too high it may cause the operation to be stuck for too
                    long rather than quickly raising a `TimeoutError` that may be recovered
                    from by the application, but under high-load a higher timeout may
                    be helpful to prevent exchanging peer info from failing too fast.

                Returns
                -------
                Listener
                    The new listener. When this object is deleted, the listening stops

        """
    def get_config(self):
        """
        Returns all UCX configuration options as a dict.

                Returns
                -------
                dict
                    The current UCX configuration options

        """
    def get_ucp_worker(self):
        """
        Returns the underlying UCP worker handle (ucp_worker_h)
                as a Python integer.

        """
    def get_ucxx_worker(self):
        """
        Returns the underlying UCXX worker pointer (ucxx::Worker*)
                as a Python integer.

        """
    def get_worker_address(self):
        ...
    def recv(self, buffer, tag):
        """
        Receive directly on worker without a local Endpoint into `buffer`.

                Parameters
                ----------
                buffer: exposing the buffer protocol or array/cuda interface
                    The buffer to receive into. Raise ValueError if buffer
                    is smaller than nbytes or read-only.
                tag: hashable, optional
                    Set a tag that must match the received message.

        """
    def start_notifier_thread(self):
        ...
    def stop_notifier_thread(self):
        """

                Stop Python future notifier thread

                Stop the notifier thread if context is running with Python future
                notification enabled via `UCXPY_ENABLE_PYTHON_FUTURE=1` or
                `ucxx.init(..., enable_python_future=True)`.

                .. warning:: When the notifier thread is enabled it may be necessary to
                             explicitly call this method before shutting down the process or
                             or application, otherwise it may block indefinitely waiting for
                             the thread to terminate. Executing `ucxx.reset()` will also run
                             this method, so it's not necessary to have both.

        """
    @property
    def config(self):
        """
        UCX configuration options as a dict.
        """
    @property
    def ucp_context_info(self):
        """
        Low-level UCX info about this endpoint as a string.
        """
    @property
    def ucp_worker(self):
        """
        The underlying UCP worker handle (ucp_worker_h) as a Python integer.
        """
    @property
    def ucp_worker_info(self):
        """
        Return low-level UCX info about this endpoint as a string.
        """
    @property
    def ucxx_worker(self):
        """
        The underlying UCXX worker pointer (ucxx::Worker*) as a Python integer.
        """
    @property
    def worker_address(self):
        ...
def clear_progress_tasks():
    ...
ProgressTasks: dict = {}
logger: logging.Logger  # value = <Logger ucx (WARNING)>
