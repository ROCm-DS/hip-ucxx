from __future__ import annotations
import gc as gc
import logging as logging
import os as os
import re as re
from ucxx import UCXXError as UCXError
from ucxx._lib import libucxx as ucx_api
from ucxx._lib_async.application_context import ApplicationContext
import weakref as weakref
__all__: list[str] = ['ApplicationContext', 'UCXError', 'continuous_ucx_progress', 'create_endpoint', 'create_endpoint_from_worker_address', 'create_listener', 'gc', 'get_active_transports', 'get_config', 'get_ucp_context_info', 'get_ucp_worker', 'get_ucp_worker_info', 'get_ucx_address_from_buffer', 'get_ucx_version', 'get_ucxx_worker', 'get_worker_address', 'init', 'logger', 'logging', 'os', 'progress', 're', 'recv', 'reset', 'stop_notifier_thread', 'ucx_api', 'weakref']
def _get_ctx():
    ...
def continuous_ucx_progress(event_loop = None):
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
def create_endpoint(ip_address, port, endpoint_error_handling = True, connect_timeout = 5.0):
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
def create_endpoint_from_worker_address(address, endpoint_error_handling = True):
    ...
def create_listener(callback_func, port = None, endpoint_error_handling = True, connect_timeout = 5.0):
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
def get_active_transports():
    """
    Returns a list of all transports that are available and are currently
        active in UCX, meaning UCX **may** use them depending on the type of
        transfers and how it is configured but is not required to do so.

    """
def get_config():
    """
    Returns all UCX configuration options as a dict.

        If UCX is uninitialized, the options returned are the
        options used if UCX were to be initialized now.
        Notice, this function doesn't initialize UCX.

        Returns
        -------
        dict
            The current UCX configuration options

    """
def get_ucp_context_info():
    """
    Gets information on the current UCX context, obtained from
        `ucp_context_print_info`.

    """
def get_ucp_worker():
    """
    Returns the underlying UCP worker handle (ucp_worker_h)
            as a Python integer.

    """
def get_ucp_worker_info():
    """
    Gets information on the current UCX worker, obtained from
        `ucp_worker_print_info`.

    """
def get_ucx_address_from_buffer(buffer):
    ...
def get_ucx_version():
    """
    Return the version of the underlying UCX installation

        Notice, this function doesn't initialize UCX.

        Returns
        -------
        tuple
            The version as a tuple e.g. (1, 7, 0)

    """
def get_ucxx_worker():
    ...
def get_worker_address():
    ...
def init(options = {}, env_takes_precedence = False, progress_mode = None, enable_delayed_submission = None, enable_python_future = None, connect_timeout = None):
    """
    Initiate UCX.

        Usually this is done automatically at the first API call
        but this function makes it possible to set UCX options programmable.
        Alternatively, UCX options can be specified through environment variables.

        Parameters
        ----------
        options: dict, optional
            UCX options send to the underlying UCX library
        env_takes_precedence: bool, optional
            Whether environment variables takes precedence over the `options`
            specified here.
        progress_mode: string, optional
            If None, thread UCX progress mode is used unless the environment variable
            `UCXPY_PROGRESS_MODE` is defined. Otherwise the options are 'blocking',
            'polling', 'thread'.
        enable_delayed_submission: boolean, optional
            If None, delayed submission is disabled unless
            `UCXPY_ENABLE_DELAYED_SUBMISSION` is defined with a value other than `0`.
        enable_python_future: boolean, optional
            If None, request notification via Python futures is disabled unless
            `UCXPY_ENABLE_PYTHON_FUTURE` is defined with a value other than `0`.
        connect_timeout: float, optional
            The timeout in seconds for exchanging endpoint information upon endpoint
            establishment. If None, use the value from `UCXPY_CONNECT_TIMEOUT` if defined,
            otherwise fallback to the default of 5 seconds.


    """
def progress():
    """
    Try to progress the communication layer

        Warning, it is illegal to call this from a call-back function such as
        the call-back function given to create_listener.

    """
def recv(buffer, tag):
    ...
def reset():
    """
    Resets the UCX library by shutting down all of UCX.

        The library is initiated at next API call.

    """
def stop_notifier_thread():
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
_ctx = None
logger: logging.Logger  # value = <Logger ucx (WARNING)>
