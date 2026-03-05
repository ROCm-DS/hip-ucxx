from __future__ import annotations
import asyncio as asyncio
from functools import partial
import socket as socket
import time as time
import ucxx._lib.libucxx
from ucxx._lib.libucxx import UCXWorker
import weakref as weakref
__all__: list[str] = ['BlockingMode', 'PollingMode', 'ProgressTask', 'ThreadMode', 'UCXWorker', 'asyncio', 'partial', 'socket', 'time', 'weakref']
class BlockingMode(ProgressTask):
    def __init__(self, worker: ucxx._lib.libucxx.UCXWorker, event_loop: asyncio.events.AbstractEventLoop, progress_timeout: float = 1.0):
        """
        Progress the UCX worker in blocking mode.

                The blocking progress mode ensure the worker is progresses whenever the
                UCX worker reports an event on its epoll file descriptor. In certain
                circumstances the epoll file descriptor may not present an event, thus
                the `progress_timeout` will ensure the UCX worker is progressed to
                prevent a potential deadlock.

                Parameters
                ----------
                worker: UCXWorker
                    Worker object from the UCXX Cython API to progress.
                event_loop: asyncio.AbstractEventLoop
                    Asynchronous event loop where to schedule async tasks.
                progress_timeout: float
                    The timeout to sleep until calling checking again whether the worker should
                    be progressed.

        """
    def _arm_worker(self):
        """
        Progress the worker and rearm.

                Progress and rearm the worker to watch for new events on its epoll file
                descriptor.

        """
    def _clear_tasks(self):
        ...
    def _fd_reader_callback(self):
        """
        Schedule new progress task upon worker event.

                Schedule new progress task when a new event occurs in the worker's epoll file
                descriptor.

        """
    def _progress_with_timeout(self):
        """
        Protect worker from never progressing again.

                To ensure the worker progresses if no events are raised and the asyncio loop
                getting stuck we must ensure the worker is progressed every so often. This
                method ensures the worker is progressed independent of what the epoll file
                descriptor does if longer than `self._progress_timeout` has elapsed since
                last check, thus preventing a deadlock.

        """
    @property
    def _tasks(self):
        ...
class PollingMode(ProgressTask):
    def __init__(self, worker, event_loop):
        ...
    def _clear_tasks(self):
        ...
    def _progress_task(self):
        """
        This helper function maintains a UCX progress loop.
        """
    @property
    def _tasks(self):
        ...
class ProgressTask:
    def __eq__(self, other):
        ...
    def __hash__(self):
        ...
    def __init__(self, worker, event_loop):
        """
        Creates a task that keeps calling worker.progress()

                Notice, class and created task is careful not to hold a
                reference to `worker` so that a danling progress task will
                not prevent `worker` to be garbage collected.

                Parameters
                ----------
                worker: UCXWorker
                    The UCX worker context to progress
                event_loop: asyncio.EventLoop
                    The event loop to do progress in.

        """
    def _clear_tasks(self) -> None:
        ...
    @property
    def _tasks(self) -> tuple[_asyncio.Task]:
        ...
class ThreadMode(ProgressTask):
    def __init__(self, worker, event_loop, polling_mode = False):
        ...
def _cancel_task(event_loop, task):
    ...
def _create_context():
    ...
