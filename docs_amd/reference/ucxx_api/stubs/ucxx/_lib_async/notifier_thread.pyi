from __future__ import annotations
import asyncio as asyncio
from builtins import TimeoutError
import logging as logging
from ucxx._lib import libucxx as ucx_api
__all__: list[str] = ['TimeoutError', 'asyncio', 'logger', 'logging', 'ucx_api']
def _notifierThread(event_loop, worker, q):
    ...
def _notifier_coroutine(worker):
    ...
def _run_request_notifier(worker):
    ...
logger: logging.Logger  # value = <Logger ucx (WARNING)>
