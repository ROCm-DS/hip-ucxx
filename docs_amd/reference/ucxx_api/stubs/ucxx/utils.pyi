from __future__ import annotations
from contextlib import contextmanager
from dask.utils import format_bytes
from dask.utils import format_time
from dask.utils import parse_bytes
import fcntl as fcntl
import glob as glob
import logging as logging
import multiprocessing.context
import numpy as np
import os as os
import socket as socket
import struct as struct
import time as time
__all__: list[str] = ['contextmanager', 'fcntl', 'format_bytes', 'format_time', 'get_address', 'get_ucxpy_logger', 'glob', 'hmean', 'logging', 'mp', 'np', 'nvtx_annotate', 'os', 'parse_bytes', 'print_key_value', 'print_multi', 'print_separator', 'socket', 'struct', 'time']
def get_address(ifname = None, use_ipv6 = False):
    """

        Get the address associated with a network interface.

        Parameters
        ----------
        ifname : str
            The network interface name to find the address for.
            If None, it uses the value of environment variable `UCXPY_IFNAME`
            and if `UCXPY_IFNAME` is not set it defaults to "ib0"
            An OSError is raised for invalid interfaces.
        use_ipv6 : bool
            Whether to get IPv6 addresses instead of the IPv4 default.
            NOTE: Requires the `psutil` package.

        Raises
        ------
        OSError
            If no device was found with the specified `ifname`, or no suitable
            devices were found when `ifname=None`.

        Returns
        -------
        address : str
            The inet addr associated with an interface.

        Examples
        --------
        >>> get_address()
        '10.33.225.160'

        >>> get_address(ifname='lo')
        '127.0.0.1'

        >>> get_address(ifname='lo', use_ipv6=True)
        '::1'

    """
def get_ucxpy_logger():
    """

        Get UCX-Py logger with custom formatting

        Returns
        -------
        logger : logging.Logger
            Logger object

        Examples
        --------
        >>> logger = get_ucxpy_logger()
        >>> logger.warning("Test")
        [1585175070.2911468] [dgx12:1054] UCXPY  WARNING Test

    """
def hmean(a):
    """
    Harmonic mean
    """
def nvtx_annotate(*args, **kwds):
    ...
def print_key_value(key, value, key_length = 25):
    """
    Print a key and value with fixed key-field length
    """
def print_multi(values, key_length = 25):
    """
    Print a key and value with fixed key-field length
    """
def print_separator(separator = '-', length = 80):
    """
    Print a single separator character multiple times
    """
mp: multiprocessing.context.SpawnContext  # value = <multiprocessing.context.SpawnContext object>
