from __future__ import annotations
from multiprocessing.process import BaseProcess
import time as time
__all__: list[str] = ['BaseProcess', 'join_processes', 'terminate_process', 'time', 'wait_requests']
def join_processes(processes: list[typing.Type[multiprocessing.process.BaseProcess]], timeout: typing.Union[float, int]) -> None:
    """

        Join a list of processes with a combined timeout.

        Join a list of processes with a combined timeout, for each process `join()`
        is called with a timeout equal to the difference of `timeout` and the time
        elapsed since this function was called.

        Parameters
        ----------
        processes:
            The list of processes to be joined.
        timeout: float or integer
            Maximum time to wait for all the processes to be joined.

    """
def terminate_process(process: typing.Type[multiprocessing.process.BaseProcess], kill_wait: typing.Union[float, int] = 3.0) -> None:
    """

        Ensure a spawned process is terminated.

        Ensure a spawned process is really terminated to prevent the parent process
        (such as pytest) from freezing upon exit.

        Parameters
        ----------
        process:
            The process to be terminated.
        kill_wait: float or integer
            Maximum time to wait for the kill signal to terminate the process.

        Raises
        ------
        RuntimeError
            If the process terminated with a non-zero exit code.
        ValueError
            If the process was still alive after ``kill_wait`` seconds.

    """
def wait_requests(worker, progress_mode, requests):
    ...
