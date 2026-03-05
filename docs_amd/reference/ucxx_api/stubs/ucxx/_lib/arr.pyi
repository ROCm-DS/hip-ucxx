from View.MemoryView import __pyx_unpickle_Enum
from __future__ import annotations
import builtins as __builtins__
from numpy import dtype as numpy_dtype
import typing
__all__: list[str] = ['Array', 'asarray', 'numpy_dtype']
class Array:
    """
     An efficient wrapper for host and device array-like objects

        Parameters
        ----------
        obj: Object exposing the buffer protocol or __cuda_array_interface__
            A host and device array-like object

    """
    __pyx_vtable__: typing.ClassVar[typing.Any]  # value = <capsule object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def _c_contiguous(self):
        """
        Array._c_contiguous(self) -> bool
        """
    def _contiguous(self):
        """
        Array._contiguous(self) -> bool
        """
    def _f_contiguous(self):
        """
        Array._f_contiguous(self) -> bool
        """
    def _nbytes(self):
        """
        Array._nbytes(self) -> Py_ssize_t
        """
def asarray(obj):
    """
    asarray(obj) -> Array

    Coerce other objects to ``Array``. No-op for existing ``Array``s.

    Parameters
    ----------
    obj: object
        Object exposing the Python buffer protocol or ``__cuda_array_interface__``.

    Returns
    -------
    array: Array
        An instance of the ``Array`` class.
    """
__pyx_capi__: dict  # value = {'asarray': <capsule object "struct __pyx_obj_4ucxx_4_lib_3arr_Array *(PyObject *, int __pyx_skip_dispatch)" at 0x7fe754d5fed0>}
__test__: dict = {}
