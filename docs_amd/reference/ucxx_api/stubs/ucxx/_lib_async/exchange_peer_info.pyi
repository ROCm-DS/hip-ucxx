from __future__ import annotations
import asyncio as asyncio
import logging as logging
import struct as struct
from ucxx._lib.arr import Array
from ucxx._lib_async.utils import hash64bits
__all__: list[str] = ['Array', 'asyncio', 'exchange_peer_info', 'hash64bits', 'logger', 'logging', 'struct']
def exchange_peer_info(endpoint, msg_tag, listener, connect_timeout = 5.0):
    """
    Help function that exchange endpoint information
    """
logger: logging.Logger  # value = <Logger ucx (WARNING)>
