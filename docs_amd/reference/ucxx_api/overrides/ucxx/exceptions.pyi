from __future__ import annotations

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

__all__: list[str] = ['UCXAlreadyExistsError', 'UCXBufferTooSmallError', 'UCXBusyError', 'UCXCanceled', 'UCXCanceledError', 'UCXCloseError', 'UCXConfigError', 'UCXConnectionResetError', 'UCXEndpointTimeoutError', 'UCXError', 'UCXExceedsLimitError', 'UCXFirstEndpointFailureError', 'UCXFirstLinkFailureError', 'UCXIOError', 'UCXInvalidAddrError', 'UCXInvalidParamError', 'UCXLastEndpointFailureError', 'UCXLastLinkFailureError', 'UCXMessageTruncatedError', 'UCXMsgTruncated', 'UCXNoDeviceError', 'UCXNoElemError', 'UCXNoMemoryError', 'UCXNoMessageError', 'UCXNoProgressError', 'UCXNoResourceError', 'UCXNotConnectedError', 'UCXNotImplementedError', 'UCXOutOfRangeError', 'UCXRejectedError', 'UCXShmemSegmentError', 'UCXSomeConnectsFailedError', 'UCXTimedOutError', 'UCXUnreachableError', 'UCXUnsupportedError']
