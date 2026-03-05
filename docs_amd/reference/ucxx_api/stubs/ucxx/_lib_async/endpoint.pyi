from __future__ import annotations
import array as array
import asyncio as asyncio
import logging as logging
from ucxx import UCXXCanceledError as UCXCanceled
from ucxx import UCXXCloseError as UCXCloseError
from ucxx import UCXXError as UCXError
from ucxx._lib.arr import Array
import ucxx._lib.libucxx
from ucxx._lib import libucxx as ucx_api
from ucxx._lib.libucxx import UCXXTag as Tag
from ucxx._lib_async.utils import hash64bits
import warnings as warnings
import weakref as weakref
__all__: list[str] = ['Array', 'Endpoint', 'Tag', 'TagMaskFull', 'UCXCanceled', 'UCXCloseError', 'UCXError', 'array', 'asyncio', 'hash64bits', 'logger', 'logging', 'ucx_api', 'warnings', 'weakref']
class Endpoint:
    """
    An endpoint represents a connection to a peer

        Please use `create_listener()` and `create_endpoint()`
        to create an Endpoint.

    """
    def __init__(self, endpoint, ctx, tags = None):
        ...
    def abort(self, period = 10000000000, max_attempts = 1):
        """
        Close the communication immediately and abruptly.
                Useful in destructors or generators' ``finally`` blocks.

                Despite the attempt to close communication immediately, in some
                circumstances, notably when the parent worker is running a progress
                thread, a maximum timeout may be specified for which the close operation
                will wait. This can be particularly important for cases where the progress
                thread might be attempting to acquire the GIL while the current
                thread owns that resource.

                Notice, this functions doesn't signal the connected peer to close.
                To do that, use `Endpoint.close()`.

                Parameters
                ----------
                period: int
                    maximum period to wait (in ns) for internal endpoint operations
                    to complete, usually two operations (pre and post) are involved
                    thus the maximum perceived timeout should be multiplied by two.
                max_attempts: int
                    maximum number of attempts to close endpoint, only applicable
                    if worker is running a progress thread and `period > 0`.

        """
    def am_recv(self):
        """
        Receive from connected peer via active messages.
        """
    def am_send(self, buffer):
        """
        Send `buffer` to connected peer via active messages.

                Parameters
                ----------
                buffer: exposing the buffer protocol or array/cuda interface
                    The buffer to send. Raise ValueError if buffer is smaller
                    than nbytes.

        """
    def close(self, period = 10000000000, max_attempts = 1):
        """
        Close the endpoint cleanly.
                This will attempt to flush outgoing buffers before actually
                closing the underlying UCX endpoint.

                A maximum timeout and number of attempts may be specified to prevent the
                underlying `Endpoint` object from failing to acquire the GIL, see `abort()`
                for details.

                Parameters
                ----------
                period: int
                    maximum period to wait (in ns) for internal endpoint operations
                    to complete, usually two operations (pre and post) are involved
                    thus the maximum perceived timeout should be multiplied by two.
                max_attempts: int
                    maximum number of attempts to close endpoint, only applicable
                    if worker is running a progress thread and `period > 0`.

        """
    def close_after_n_recv(self, n, count_from_ep_creation = False):
        """
        Close the endpoint after `n` received messages.

                Parameters
                ----------
                n: int
                    Number of messages to received before closing the endpoint.
                count_from_ep_creation: bool, optional
                    Whether to count `n` from this function call (default) or
                    from the creation of the endpoint.

        """
    def get_ucp_endpoint(self):
        """
        Returns the underlying UCP endpoint handle (ucp_ep_h)
                as a Python integer.

        """
    def get_ucp_worker(self):
        """
        Returns the underlying UCP worker handle (ucp_worker_h)
                as a Python integer.

        """
    def get_ucxx_endpoint(self):
        """
        Returns the underlying UCXX endpoint pointer (ucxx::Endpoint*)
                as a Python integer.

        """
    def get_ucxx_worker(self):
        """
        Returns the underlying UCXX worker pointer (ucxx::Worker*)
                as a Python integer.

        """
    def is_alive(self):
        ...
    def recv(self, buffer, tag = None, force_tag = False):
        """
        Receive from connected peer into `buffer`.

                Parameters
                ----------
                buffer: exposing the buffer protocol or array/cuda interface
                    The buffer to receive into. Raise ValueError if buffer
                    is smaller than nbytes or read-only.
                tag: hashable, optional
                    Set a tag that must match the received message. Currently
                    the tag is hashed together with the internal Endpoint tag
                    that is agreed with the remote end at connection time.
                    To enforce using the user tag, make sure to specify
                    `force_tag=True`.
                force_tag: bool
                    If true, force using `tag` as is, otherwise the value
                    specified with `tag` (if any) will be hashed with the
                    internal Endpoint tag.

        """
    def recv_multi(self, tag = None, force_tag = False):
        """
        Receive from connected peer into `buffer`.

                Parameters
                ----------
                tag: hashable, optional
                    Set a tag that must match the received message. Currently
                    the tag is hashed together with the internal Endpoint tag
                    that is agreed with the remote end at connection time.
                    To enforce using the user tag, make sure to specify
                    `force_tag=True`.
                force_tag: bool
                    If true, force using `tag` as is, otherwise the value
                    specified with `tag` (if any) will be hashed with the
                    internal Endpoint tag.

        """
    def recv_obj(self, tag = None, allocator = bytearray):
        """
        Receive from connected peer that calls `send_obj()`.

                As opposed to `recv()`, this function returns the received object.
                Data is received into a buffer allocated by `allocator`.

                The transfer includes an extra message containing the size of `obj`,
                which increases the overhead slightly.

                Parameters
                ----------
                tag: hashable, optional
                    Set a tag that must match the received message. Notice, currently
                    UCX-Py doesn't support a "any tag" thus `tag=None` only matches a
                    send that also sets `tag=None`.
                allocator: callabale, optional
                    Function to allocate the received object. The function should
                    take the number of bytes to allocate as input and return a new
                    buffer of that size as output.

                Example
                -------
                >>> await pickle.loads(ep.recv_obj())

        """
    def send(self, buffer, tag = None, force_tag = False):
        """
        Send `buffer` to connected peer.

                Parameters
                ----------
                buffer: exposing the buffer protocol or array/cuda interface
                    The buffer to send. Raise ValueError if buffer is smaller
                    than nbytes.
                tag: hashable, optional
                    Set a tag that the receiver must match. Currently the tag
                    is hashed together with the internal Endpoint tag that is
                    agreed with the remote end at connection time. To enforce
                    using the user tag, make sure to specify `force_tag=True`.
                force_tag: bool
                    If true, force using `tag` as is, otherwise the value
                    specified with `tag` (if any) will be hashed with the
                    internal Endpoint tag.

        """
    def send_multi(self, buffers, tag = None, force_tag = False):
        """
        Send `buffer` to connected peer.

                Parameters
                ----------
                buffer: exposing the buffer protocol or array/cuda interface
                    The buffer to send. Raise ValueError if buffer is smaller
                    than nbytes.
                tag: hashable, optional
                    Set a tag that the receiver must match. Currently the tag
                    is hashed together with the internal Endpoint tag that is
                    agreed with the remote end at connection time. To enforce
                    using the user tag, make sure to specify `force_tag=True`.
                force_tag: bool
                    If true, force using `tag` as is, otherwise the value
                    specified with `tag` (if any) will be hashed with the
                    internal Endpoint tag.

        """
    def send_obj(self, obj, tag = None):
        """
        Send `obj` to connected peer that calls `recv_obj()`.

                The transfer includes an extra message containing the size of `obj`,
                which increases the overhead slightly.

                Parameters
                ----------
                obj: exposing the buffer protocol or array/cuda interface
                    The object to send.
                tag: hashable, optional
                    Set a tag that the receiver must match.

                Example
                -------
                >>> await ep.send_obj(pickle.dumps([1,2,3]))

        """
    def set_close_callback(self, callback_func, cb_args = None, cb_kwargs = None):
        """
        Register a user callback function to be called on Endpoint's closing.

                Allows the user to register a callback function to be called when the
                Endpoint's error callback is called, or during its finalizer if the error
                callback is never called.

                Once the callback is called, it's not possible to send any more messages.
                However, receiving messages may still be possible, as UCP may still have
                incoming messages in transit.

                Parameters
                ----------
                callback_func: callable
                    The callback function to be called when the Endpoint's error callback
                    is called, otherwise called on its finalizer.
                cb_args: tuple or None
                    The arguments to be passed to the callback function as a `tuple`, or
                    `None` (default).
                cb_kwargs: dict or None
                    The keyword arguments to be passed to the callback function as a
                    `dict`, or `None` (default).

                Example
                >>> ep.set_close_callback(lambda: print("Executing close callback"))

        """
    @property
    def alive(self):
        ...
    @property
    def closed(self):
        """
        Is this endpoint closed?
        """
    @property
    def ucp_endpoint(self):
        """
        The underlying UCP endpoint handle (ucp_ep_h) as a Python integer.
        """
    @property
    def ucp_worker(self):
        """
        The underlying UCP worker handle (ucp_worker_h) as a Python integer.
        """
    @property
    def ucxx_endpoint(self):
        """
        The underlying UCXX endpoint pointer (ucxx::Endpoint*) as a Python
                integer.

        """
    @property
    def ucxx_worker(self):
        """
        Returns the underlying UCXX worker pointer (ucxx::Worker*)
                as a Python integer.

        """
    @property
    def uid(self):
        """
        The unique ID of the underlying UCX endpoint
        """
def _finalizer(endpoint: ucxx._lib.libucxx.UCXEndpoint) -> None:
    """
    Endpoint finalizer.

        Attempt to close the endpoint if it's still alive.

        Parameters
        ----------
        endpoint: ucx_api.UCXEndpoint
            The endpoint to close.

    """
TagMaskFull: ucxx._lib.libucxx.UCXXTagMask  # value = <ucxx._lib.libucxx.UCXXTagMask object>
logger: logging.Logger  # value = <Logger ucx (WARNING)>
