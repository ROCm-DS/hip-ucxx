from __future__ import annotations
import asyncio as asyncio
import logging as logging
import os as os
import threading as threading
from ucxx import UCXXMessageTruncatedError as UCXMessageTruncatedError
from ucxx._lib import libucxx as ucx_api
from ucxx._lib_async.endpoint import Endpoint
from ucxx._lib_async.exchange_peer_info import exchange_peer_info
from ucxx._lib_async.utils import hash64bits
import weakref as weakref
__all__: list[str] = ['ActiveClients', 'Endpoint', 'Listener', 'UCXMessageTruncatedError', 'asyncio', 'exchange_peer_info', 'hash64bits', 'logger', 'logging', 'os', 'threading', 'ucx_api', 'weakref']
class ActiveClients:
    """

        Handle number of active clients on `Listener`.

        Each `Listener` contains a unique ID that can be used to increment/decrement the
        number of currently active client handlers. Useful to warn when the `Listener` is
        being destroyed but callbacks handling clients have not yet completed, which may
        lead to errors as the `Listener` most likely ended prematurely.

    """
    def __init__(self):
        ...
    def add_listener(self, ident: int) -> None:
        ...
    def dec(self, ident: int) -> None:
        ...
    def get_active(self, ident: int) -> int:
        ...
    def inc(self, ident: int) -> None:
        ...
    def remove_listener(self, ident: int) -> None:
        ...
class Listener:
    """
    A handle to the listening service started by `create_listener()`

        The listening continues as long as this object exist or `.close()` is called.
        Please use `create_listener()` to create an Listener.

    """
    def __init__(self, listener, ident, active_clients):
        ...
    def close(self):
        """
        Closing the listener
        """
    @property
    def active_clients(self):
        ...
    @property
    def closed(self):
        """
        Is the listener closed?
        """
    @property
    def ip(self):
        """
        The listening network IP address
        """
    @property
    def port(self):
        """
        The listening network port
        """
def _finalizer(ident: int, active_clients: ActiveClients) -> None:
    """
    Listener finalizer.

        Finalize the listener and remove it from the `ActiveClients`. If there are
        active clients, a warning is logged.

        Parameters
        ----------
        ident: int
            The unique identifier of the `Listener`.
        active_clients: ActiveClients
            Instance of `ActiveClients` owned by the parent `ApplicationContext`
            from which to remove the `Listener`.

    """
def _listener_handler(conn_request, event_loop, callback_func, ctx, endpoint_error_handling, connect_timeout, ident, active_clients):
    ...
def _listener_handler_coroutine(conn_request, ctx, func, endpoint_error_handling, connect_timeout, ident, active_clients):
    ...
logger: logging.Logger  # value = <Logger ucx (WARNING)>
