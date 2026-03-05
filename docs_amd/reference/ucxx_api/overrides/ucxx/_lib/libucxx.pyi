from View.MemoryView import __pyx_unpickle_Enum
from __future__ import annotations
import asyncio as asyncio
import builtins as __builtins__
import enum as enum
import functools as functools
import logging as logging
import numpy as np
import typing
import warnings as warnings
import weakref as weakref

class UCXError(Exception):
    """Base exception for all UCX errors."""

class UCXAlreadyExistsError(UCXError):
    """Raised when a resource already exists."""

class UCXBufferTooSmallError(UCXError):
    """Raised when a buffer is too small for the requested operation."""

class UCXBusyError(UCXError):
    """Raised when a resource is busy and cannot process the request."""

class UCXCanceled(UCXError):
    """Raised when a UCX operation is canceled (legacy alias for UCXCanceledError)."""

class UCXCanceledError(UCXError):
    """Raised when a UCX operation is canceled."""

class UCXCloseError(UCXError):
    """Raised when an endpoint or connection is closed."""

class UCXConfigError(UCXError):
    """Raised when there is a UCX configuration error."""

class UCXConnectionResetError(UCXError):
    """Raised when a connection is reset by the remote peer."""

class UCXEndpointTimeoutError(UCXError):
    """Raised when an endpoint operation times out."""

class UCXExceedsLimitError(UCXError):
    """Raised when a request exceeds a configured limit."""

class UCXFirstEndpointFailureError(UCXError):
    """Raised on the first endpoint failure in a connection."""

class UCXFirstLinkFailureError(UCXError):
    """Raised on the first link failure in a connection."""

class UCXIOError(UCXError):
    """Raised when an I/O error occurs during a UCX operation."""

class UCXInvalidAddrError(UCXError):
    """Raised when an invalid address is provided."""

class UCXInvalidParamError(UCXError):
    """Raised when an invalid parameter is passed to a UCX function."""

class UCXLastEndpointFailureError(UCXError):
    """Raised on the last endpoint failure in a connection."""

class UCXLastLinkFailureError(UCXError):
    """Raised on the last link failure in a connection."""

class UCXMessageTruncatedError(UCXError):
    """Raised when a received message is truncated."""

class UCXMsgTruncated(UCXError):
    """Raised when a received message is truncated (legacy alias for UCXMessageTruncatedError)."""

class UCXNoDeviceError(UCXError):
    """Raised when no suitable device is available."""

class UCXNoElemError(UCXError):
    """Raised when the requested element is not found."""

class UCXNoMemoryError(UCXError):
    """Raised when memory allocation fails."""

class UCXNoMessageError(UCXError):
    """Raised when no message is available."""

class UCXNoProgressError(UCXError):
    """Raised when no progress can be made on the operation."""

class UCXNoResourceError(UCXError):
    """Raised when a required resource is unavailable."""

class UCXNotConnectedError(UCXError):
    """Raised when an operation requires a connection that does not exist."""

class UCXNotImplementedError(UCXError):
    """Raised when a requested feature is not implemented."""

class UCXOutOfRangeError(UCXError):
    """Raised when a value is out of the valid range."""

class UCXRejectedError(UCXError):
    """Raised when a connection or operation is rejected."""

class UCXShmemSegmentError(UCXError):
    """Raised when a shared memory segment operation fails."""

class UCXSomeConnectsFailedError(UCXError):
    """Raised when some connection attempts in a group fail."""

class UCXTimedOutError(UCXError):
    """Raised when an operation times out."""

class UCXUnreachableError(UCXError):
    """Raised when the remote destination is unreachable."""

class UCXUnsupportedError(UCXError):
    """Raised when the requested operation is not supported."""

__all__: list[str] = ['Feature', 'HostBufferAdapter', 'PythonRequestNotifierWaitState', 'UCXAddress', 'UCXAlreadyExistsError', 'UCXBufferRequest', 'UCXBufferRequests', 'UCXBufferTooSmallError', 'UCXBusyError', 'UCXCanceled', 'UCXCanceledError', 'UCXCloseError', 'UCXConfig', 'UCXConfigError', 'UCXConnectionResetError', 'UCXContext', 'UCXEndpoint', 'UCXEndpointTimeoutError', 'UCXError', 'UCXExceedsLimitError', 'UCXFirstEndpointFailureError', 'UCXFirstLinkFailureError', 'UCXIOError', 'UCXInvalidAddrError', 'UCXInvalidParamError', 'UCXLastEndpointFailureError', 'UCXLastLinkFailureError', 'UCXListener', 'UCXMessageTruncatedError', 'UCXMsgTruncated', 'UCXNoDeviceError', 'UCXNoElemError', 'UCXNoMemoryError', 'UCXNoMessageError', 'UCXNoProgressError', 'UCXNoResourceError', 'UCXNotConnectedError', 'UCXNotImplementedError', 'UCXOutOfRangeError', 'UCXRejectedError', 'UCXRequest', 'UCXShmemSegmentError', 'UCXSomeConnectsFailedError', 'UCXTimedOutError', 'UCXUnreachableError', 'UCXUnsupportedError', 'UCXWorker', 'UCXXTag', 'UCXXTagMask', 'UCXXTagMaskFull', 'asyncio', 'enum', 'functools', 'get_current_options', 'get_ucx_version', 'logger', 'logging', 'np', 'warnings', 'weakref']
class Feature(enum.Enum):
    AM: typing.ClassVar[Feature]  # value = <Feature.AM: 64>
    AMO32: typing.ClassVar[Feature]  # value = <Feature.AMO32: 4>
    AMO64: typing.ClassVar[Feature]  # value = <Feature.AMO64: 8>
    RMA: typing.ClassVar[Feature]  # value = <Feature.RMA: 2>
    STREAM: typing.ClassVar[Feature]  # value = <Feature.STREAM: 32>
    TAG: typing.ClassVar[Feature]  # value = <Feature.TAG: 1>
    WAKEUP: typing.ClassVar[Feature]  # value = <Feature.WAKEUP: 16>
class HostBufferAdapter:
    """
    A simple adapter around HostBuffer implementing the buffer protocol
    """
    __pyx_vtable__: typing.ClassVar[typing.Any]  # value = <capsule object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        """
        HostBufferAdapter.__reduce_cython__(self)
        """
    @staticmethod
    def __setstate__(*args, **kwargs):
        """
        HostBufferAdapter.__setstate_cython__(self, __pyx_state)
        """
    def __buffer__(self, flags):
        """
        Return a buffer object that exposes the underlying memory of the object.
        """
    def __release_buffer__(self, buffer):
        """
        Release the buffer object that exposes the underlying memory of the object.
        """
class PythonRequestNotifierWaitState(enum.Enum):
    Ready: typing.ClassVar[PythonRequestNotifierWaitState]  # value = <PythonRequestNotifierWaitState.Ready: 0>
    Shutdown: typing.ClassVar[PythonRequestNotifierWaitState]  # value = <PythonRequestNotifierWaitState.Shutdown: 2>
    Timeout: typing.ClassVar[PythonRequestNotifierWaitState]  # value = <PythonRequestNotifierWaitState.Timeout: 1>
class UCXAddress:
    """
    UCXAddress() -> None
    """
    __pyx_vtable__: typing.ClassVar[typing.Any]  # value = <capsule object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @classmethod
    def create_from_buffer(cls, buf) -> UCXAddress:
        """
        UCXAddress.create_from_buffer(cls, bytes buf) -> UCXAddress
        """
    @classmethod
    def create_from_worker(cls, worker) -> UCXAddress:
        """
        UCXAddress.create_from_worker(cls, UCXWorker worker) -> UCXAddress
        """
    @classmethod
    def from_worker(cls, worker) -> UCXAddress:
        """
        UCXAddress.from_worker(cls, UCXWorker worker) -> UCXAddress
        """
    def __buffer__(self, flags):
        """
        Return a buffer object that exposes the underlying memory of the object.
        """
    def __bytes__(self) -> bytes:
        """
        UCXAddress.__bytes__(self) -> bytes
        """
    def __hash__(self):
        """
        Return hash(self).
        """
    def __reduce__(self) -> tuple:
        """
        UCXAddress.__reduce__(self) -> tuple
        """
    def __release_buffer__(self, buffer):
        """
        Release the buffer object that exposes the underlying memory of the object.
        """
class UCXBufferRequest:
    """
    UCXBufferRequest(uintptr_t shared_ptr_buffer_request, bool enable_python_future) -> None
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        """
        UCXBufferRequest.__reduce_cython__(self)
        """
    @staticmethod
    def __setstate__(*args, **kwargs):
        """
        UCXBufferRequest.__setstate_cython__(self, __pyx_state)
        """
    def get_py_buffer(self) -> None | np.ndarray | DeviceBuffer:
        """
        UCXBufferRequest.get_py_buffer(self) -> None | np.ndarray | DeviceBuffer
        """
    def get_request(self) -> UCXRequest:
        """
        UCXBufferRequest.get_request(self) -> UCXRequest
        """
class UCXBufferRequests:
    """
    UCXBufferRequests(uintptr_t unique_ptr_buffer_requests, bool enable_python_future) -> None
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        """
        UCXBufferRequests.__reduce_cython__(self)
        """
    @staticmethod
    def __setstate__(*args, **kwargs):
        """
        UCXBufferRequests.__setstate_cython__(self, __pyx_state)
        """
    def _populate_requests(self) -> None:
        """
        UCXBufferRequests._populate_requests(self) -> None
        """
    def check_error(self) -> None:
        """
        UCXBufferRequests.check_error(self) -> None
        """
    def get_future(self) -> typing.Any:
        """
        UCXBufferRequests.get_future(self) -> object
        """
    def get_py_buffers(self) -> tuple[None | np.ndarray | DeviceBuffer, ...]:
        """
        UCXBufferRequests.get_py_buffers(self) -> tuple[None | np.ndarray | DeviceBuffer, ...]
        """
    def get_requests(self) -> tuple[UCXRequest, ...]:
        """
        UCXBufferRequests.get_requests(self) -> tuple[UCXRequest, ...]
        """
    def get_status(self) -> ucs_status_t:
        """
        UCXBufferRequests.get_status(self) -> ucs_status_t
        """
    def is_completed(self) -> bool:
        """
        UCXBufferRequests.is_completed(self) -> bool
        """
    def is_completed_all(self) -> bool:
        """
        UCXBufferRequests.is_completed_all(self) -> bool
        """
    def wait(self) -> None:
        """
        UCXBufferRequests.wait(self) -> None
        """
    def wait_yield(self) -> None:
        """
        UCXBufferRequests.wait_yield(self) -> None
        """
class UCXConfig:
    """
    UCXConfig(ConfigMap user_options=ConfigMap()) -> None
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        """
        UCXConfig.__reduce_cython__(self)
        """
    @staticmethod
    def __setstate__(*args, **kwargs):
        """
        UCXConfig.__setstate_cython__(self, __pyx_state)
        """
    def get(self) -> dict:
        """
        UCXConfig.get(self) -> dict
        """
class UCXContext:
    """
    UCXContext(dict config_dict=None, tuple feature_flags=(Feature.TAG, Feature.WAKEUP, Feature.STREAM, Feature.AM, Feature.RMA)) -> None

    Python representation of `ucp_context_h`

    Parameters
    ----------
    config_dict: Mapping[str, str]
        UCX options such as "MEMTYPE_CACHE=n" and "SEG_SIZE=3M"
    feature_flags: Iterable[Feature]
        Tuple of UCX feature flags
    """
    __pyx_vtable__: typing.ClassVar[typing.Any]  # value = <capsule object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        """
        UCXContext.__reduce_cython__(self)
        """
    @staticmethod
    def __setstate__(*args, **kwargs):
        """
        UCXContext.__setstate_cython__(self, __pyx_state)
        """
    def get_config(self):
        """
        UCXContext.get_config(self) -> dict
        """
class UCXEndpoint:
    """
    UCXEndpoint() -> None
    """
    __pyx_vtable__: typing.ClassVar[typing.Any]  # value = <capsule object>
    _no_cuda_support_message: typing.ClassVar[str] = 'UCX is not configured with CUDA/ROCm support, please ensure that the available UCX on your environment is built against CUDA or ROCm and that `cuda/rocm` or `cuda_copy/rocm_copy` are present in `UCX_TLS` or that it is using the default `UCX_TLS=all`.'
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        """
        UCXEndpoint.__reduce_cython__(self)
        """
    @staticmethod
    def __setstate__(*args, **kwargs):
        """
        UCXEndpoint.__setstate_cython__(self, __pyx_state)
        """
    @classmethod
    def create(cls, worker, ip_address, port, endpoint_error_handling) -> UCXEndpoint:
        """
        UCXEndpoint.create(cls, UCXWorker worker, str ip_address, uint16_t port, bool endpoint_error_handling) -> UCXEndpoint
        """
    @classmethod
    def create_from_conn_request(cls, listener, conn_request, endpoint_error_handling) -> UCXEndpoint:
        """
        UCXEndpoint.create_from_conn_request(cls, UCXListener listener, uintptr_t conn_request, bool endpoint_error_handling) -> UCXEndpoint
        """
    @classmethod
    def create_from_worker_address(cls, worker, address, endpoint_error_handling) -> UCXEndpoint:
        """
        UCXEndpoint.create_from_worker_address(cls, UCXWorker worker, UCXAddress address, bool endpoint_error_handling) -> UCXEndpoint
        """
    def am_probe(self) -> bool:
        """
        UCXEndpoint.am_probe(self) -> bool
        """
    def am_recv(self) -> UCXRequest:
        """
        UCXEndpoint.am_recv(self) -> UCXRequest
        """
    def am_send(self, arr) -> UCXRequest:
        """
        UCXEndpoint.am_send(self, Array arr) -> UCXRequest
        """
    def close(self) -> None:
        """
        UCXEndpoint.close(self) -> None
        """
    def close_blocking(self, period = 0, max_attempts = 1) -> None:
        """
        UCXEndpoint.close_blocking(self, uint64_t period=0, uint64_t max_attempts=1) -> None
        """
    def is_alive(self) -> bool:
        """
        UCXEndpoint.is_alive(self) -> bool
        """
    def raise_on_error(self) -> None:
        """
        UCXEndpoint.raise_on_error(self) -> None
        """
    def remove_close_callback(self) -> None:
        """
        UCXEndpoint.remove_close_callback(self) -> None
        """
    def set_close_callback(self, cb_func, cb_args = None, cb_kwargs = None) -> None:
        """
        UCXEndpoint.set_close_callback(self, cb_func, tuple cb_args=None, dict cb_kwargs=None) -> None
        """
    def stream_recv(self, arr) -> UCXRequest:
        """
        UCXEndpoint.stream_recv(self, Array arr) -> UCXRequest
        """
    def stream_send(self, arr) -> UCXRequest:
        """
        UCXEndpoint.stream_send(self, Array arr) -> UCXRequest
        """
    def tag_recv(self, arr, tag, tag_mask = ...) -> UCXRequest:
        """
        UCXEndpoint.tag_recv(self, Array arr, UCXXTag tag, UCXXTagMask tag_mask=UCXXTagMaskFull) -> UCXRequest
        """
    def tag_recv_multi(self, tag, tag_mask = ...) -> UCXBufferRequests:
        """
        UCXEndpoint.tag_recv_multi(self, UCXXTag tag, UCXXTagMask tag_mask=UCXXTagMaskFull) -> UCXBufferRequests
        """
    def tag_send(self, arr, tag) -> UCXRequest:
        """
        UCXEndpoint.tag_send(self, Array arr, UCXXTag tag) -> UCXRequest
        """
    def tag_send_multi(self, arrays, tag) -> UCXBufferRequests:
        """
        UCXEndpoint.tag_send_multi(self, tuple arrays, UCXXTag tag) -> UCXBufferRequests
        """
class UCXListener:
    """
    UCXListener() -> None
    """
    __pyx_vtable__: typing.ClassVar[typing.Any]  # value = <capsule object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        """
        UCXListener.__reduce_cython__(self)
        """
    @staticmethod
    def __setstate__(*args, **kwargs):
        """
        UCXListener.__setstate_cython__(self, __pyx_state)
        """
    @classmethod
    def create(cls, worker, port, cb_func, cb_args = None, cb_kwargs = None, deliver_endpoint = False) -> UCXListener:
        """
        UCXListener.create(cls, UCXWorker worker, uint16_t port, cb_func, tuple cb_args=None, dict cb_kwargs=None, bool deliver_endpoint=False) -> UCXListener
        """
    def create_endpoint_from_conn_request(self, conn_request, endpoint_error_handling) -> UCXEndpoint:
        """
        UCXListener.create_endpoint_from_conn_request(self, uintptr_t conn_request, bool endpoint_error_handling) -> UCXEndpoint
        """
    def is_python_future_enabled(self) -> bool:
        """
        UCXListener.is_python_future_enabled(self) -> bool
        """
class UCXRequest:
    """
    UCXRequest(uintptr_t shared_ptr_request, bool enable_python_future) -> None
    """
    __pyx_vtable__: typing.ClassVar[typing.Any]  # value = <capsule object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        """
        UCXRequest.__reduce_cython__(self)
        """
    @staticmethod
    def __setstate__(*args, **kwargs):
        """
        UCXRequest.__setstate_cython__(self, __pyx_state)
        """
    def check_error(self) -> None:
        """
        UCXRequest.check_error(self) -> None
        """
    def get_future(self) -> typing.Any:
        """
        UCXRequest.get_future(self) -> object
        """
    def get_recv_buffer(self) -> None | np.ndarray | DeviceBuffer:
        """
        UCXRequest.get_recv_buffer(self) -> None | np.ndarray | DeviceBuffer
        """
    def get_status(self) -> ucs_status_t:
        """
        UCXRequest.get_status(self) -> ucs_status_t
        """
    def is_completed(self) -> bool:
        """
        UCXRequest.is_completed(self) -> bool
        """
    def wait(self) -> None:
        """
        UCXRequest.wait(self) -> None
        """
    def wait_yield(self) -> None:
        """
        UCXRequest.wait_yield(self) -> None
        """
class UCXWorker:
    """
    UCXWorker(UCXContext context, bool enable_delayed_submission=False, bool enable_python_future=False) -> None

    Python representation of `ucp_worker_h`
    """
    __pyx_vtable__: typing.ClassVar[typing.Any]  # value = <capsule object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        """
        UCXWorker.__reduce_cython__(self)
        """
    @staticmethod
    def __setstate__(*args, **kwargs):
        """
        UCXWorker.__setstate_cython__(self, __pyx_state)
        """
    def arm(self) -> bool:
        """
        UCXWorker.arm(self) -> bool
        """
    def cancel_inflight_requests(self, period = 0, max_attempts = 1) -> int:
        """
        UCXWorker.cancel_inflight_requests(self, uint64_t period=0, uint64_t max_attempts=1) -> int
        """
    def clear_python_futures_pool(self) -> None:
        """
        UCXWorker.clear_python_futures_pool(self) -> None
        """
    def create_endpoint_from_hostname(self, ip_address, port, endpoint_error_handling) -> UCXEndpoint:
        """
        UCXWorker.create_endpoint_from_hostname(self, str ip_address, uint16_t port, bool endpoint_error_handling) -> UCXEndpoint
        """
    def create_endpoint_from_worker_address(self, address, endpoint_error_handling) -> UCXEndpoint:
        """
        UCXWorker.create_endpoint_from_worker_address(self, UCXAddress address, bool endpoint_error_handling) -> UCXEndpoint
        """
    def get_address(self) -> UCXAddress:
        """
        UCXWorker.get_address(self) -> UCXAddress
        """
    def init_blocking_progress_mode(self) -> None:
        """
        UCXWorker.init_blocking_progress_mode(self) -> None
        """
    def is_delayed_submission_enabled(self) -> bool:
        """
        UCXWorker.is_delayed_submission_enabled(self) -> bool
        """
    def is_python_future_enabled(self) -> bool:
        """
        UCXWorker.is_python_future_enabled(self) -> bool
        """
    def populate_python_futures_pool(self) -> None:
        """
        UCXWorker.populate_python_futures_pool(self) -> None
        """
    def progress(self) -> None:
        """
        UCXWorker.progress(self) -> None
        """
    def progress_once(self) -> bool:
        """
        UCXWorker.progress_once(self) -> bool
        """
    def progress_worker_event(self, epoll_timeout = -1) -> None:
        """
        UCXWorker.progress_worker_event(self, int epoll_timeout=-1) -> None
        """
    def run_request_notifier(self) -> None:
        """
        UCXWorker.run_request_notifier(self) -> None
        """
    def set_progress_thread_start_callback(self, cb_func, cb_args = None, cb_kwargs = None) -> None:
        """
        UCXWorker.set_progress_thread_start_callback(self, cb_func, tuple cb_args=None, dict cb_kwargs=None) -> None
        """
    def start_progress_thread(self, polling_mode = False, epoll_timeout = -1) -> None:
        """
        UCXWorker.start_progress_thread(self, bool polling_mode=False, int epoll_timeout=-1) -> None
        """
    def stop_progress_thread(self) -> None:
        """
        UCXWorker.stop_progress_thread(self) -> None
        """
    def stop_request_notifier_thread(self) -> None:
        """
        UCXWorker.stop_request_notifier_thread(self) -> None
        """
    def tag_probe(self, tag, tag_mask = ...) -> bool:
        """
        UCXWorker.tag_probe(self, UCXXTag tag, UCXXTagMask tag_mask=UCXXTagMaskFull) -> bool
        """
    def tag_recv(self, arr, tag, tag_mask = ...) -> UCXRequest:
        """
        UCXWorker.tag_recv(self, Array arr, UCXXTag tag, UCXXTagMask tag_mask=UCXXTagMaskFull) -> UCXRequest
        """
    def wait_request_notifier(self, period_ns = 0) -> PythonRequestNotifierWaitState:
        """
        UCXWorker.wait_request_notifier(self, uint64_t period_ns=0) -> PythonRequestNotifierWaitState
        """
class UCXXTag:
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        """
        UCXXTag.__reduce_cython__(self)
        """
    @staticmethod
    def __setstate__(*args, **kwargs):
        """
        UCXXTag.__setstate_cython__(self, __pyx_state)
        """
class UCXXTagMask:
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        """
        UCXXTagMask.__reduce_cython__(self)
        """
    @staticmethod
    def __setstate__(*args, **kwargs):
        """
        UCXXTagMask.__setstate_cython__(self, __pyx_state)
        """
def __reduce_cython__(self):
    """
    UCXListener.__reduce_cython__(self)
    """
def __setstate_cython__(self, __pyx_state):
    """
    UCXListener.__setstate_cython__(self, __pyx_state)
    """
def _create_exceptions():
    """
    _create_exceptions()
    """
def _get_host_buffer(recv_buffer_ptr):
    """
    _get_host_buffer(uintptr_t recv_buffer_ptr)
    """
def _get_rmm_buffer(recv_buffer_ptr):
    """
    _get_rmm_buffer(uintptr_t recv_buffer_ptr)
    """
def get_current_options() -> dict:
    """
    get_current_options() -> dict

    Returns the current UCX options
    if UCX were to be initialized now.
    """
def get_ucx_version() -> tuple[int, int, int]:
    """
    get_ucx_version() -> tuple[int, int, int]
    """
UCXXTagMaskFull: UCXXTagMask  # value = <ucxx._lib.libucxx.UCXXTagMask object>
__test__: dict = {}
logger: logging.Logger  # value = <Logger ucx (WARNING)>
