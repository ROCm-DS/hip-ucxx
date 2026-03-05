"""
UCXX: Python bindings for the Unified Communication X library (UCX <www.openucx.org>)
"""
from __future__ import annotations
import ctypes
import gc as gc
import logging as logging
import numba as numba
import os as os
import pynvml as pynvml
import re as re
from ucxx._lib import libucxx as ucx_api
from ucxx._lib import libucxx
from ucxx._lib_async.application_context import ApplicationContext
from ucxx.core import continuous_ucx_progress
from ucxx.core import create_endpoint
from ucxx.core import create_endpoint_from_worker_address
from ucxx.core import create_listener
from ucxx.core import get_active_transports
from ucxx.core import get_config
from ucxx.core import get_ucp_context_info
from ucxx.core import get_ucp_worker
from ucxx.core import get_ucp_worker_info
from ucxx.core import get_ucx_address_from_buffer
from ucxx.core import get_ucx_version
from ucxx.core import get_ucxx_worker
from ucxx.core import get_worker_address
from ucxx.core import init
from ucxx.core import progress
from ucxx.core import recv
from ucxx.core import reset
from ucxx.core import stop_notifier_thread
from ucxx.utils import get_address
from ucxx.utils import get_ucxpy_logger
from ucxx.exceptions import UCXError as UCXError
import weakref as weakref
from . import _lib
from . import _lib_async
from . import _version
from . import core
from . import exceptions
from . import testing
from . import types
from . import utils
__all__: list[str] = ['ApplicationContext', 'UCXError', 'continuous_ucx_progress', 'core', 'create_endpoint', 'create_endpoint_from_worker_address', 'create_listener', 'dev_idx', 'device_count', 'exceptions', 'gc', 'get_active_transports', 'get_address', 'get_config', 'get_ucp_context_info', 'get_ucp_worker', 'get_ucp_worker_info', 'get_ucx_address_from_buffer', 'get_ucx_version', 'get_ucxpy_logger', 'get_ucxx_worker', 'get_worker_address', 'handle', 'init', 'large_bar1', 'libucxx', 'logger', 'logging', 'numba', 'os', 'progress', 'pynvml', 're', 'recv', 'reset', 'stop_notifier_thread', 'testing', 'total_memory', 'types', 'ucx_api', 'utils', 'weakref']
def _is_mig_device(handle):
    ...
__git_commit__: str = ''
__ucx_min_version__: str = '1.17.0'
__ucx_version__: str = '1.18.1'
__version__: str = '00.01.00'
_ucx_version: tuple = (1, 18, 1)
dev_idx: int = 7
device_count: int = 8
handle: ctypes.c_void_p  # value = c_void_p(73314112)
large_bar1: list = [False, False, False, False, False, False, False, False]
logger: logging.Logger  # value = <Logger ucx (WARNING)>
total_memory: int = 68702699520
