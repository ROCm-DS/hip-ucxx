from __future__ import annotations
import asyncio as asyncio
import hashlib as hashlib
import multiprocessing.context
__all__: list[str] = ['asyncio', 'get_event_loop', 'hash64bits', 'hashlib', 'mp']
def get_event_loop():
    """

        Get running or create new event loop

        In Python 3.10, the behavior of `get_event_loop()` is deprecated and in
        the future it will be an alias of `get_running_loop()`. In several
        situations, UCX-Py needs to create a new event loop, so this function
        will remain for now as an alternative to the behavior of `get_event_loop()`
        from Python < 3.10, returning the `get_running_loop()` if an event loop
        exists, or returning a new one with `new_event_loop()` otherwise.

    """
def hash64bits(*args):
    """
    64 bit unsigned hash of `args`
    """
mp: multiprocessing.context.SpawnContext  # value = <multiprocessing.context.SpawnContext object>
