from typing import *
from hydpy.core import typingtools

Input = Union[float, Double, PDouble]

class DoubleBase:
    def __neg__(self) -> Double: ...
    def __pos__(self) -> Double: ...
    def __abs__(self) -> Double: ...
    def __invert__(self) -> Double: ...
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __lt__(self, other: Input) -> bool: ...
    def __le__(self, other: Input) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __ge__(self, other: Input) -> bool: ...
    def __gt__(self, other: Input) -> bool: ...

class Double(DoubleBase):
    def __init__(self, value: float) -> None: ...
    def setvalue(self, value: Input) -> None: ...
    def __getitem__(self, key: int) -> float: ...
    def __setitem__(self, key: int, value: Input) -> None: ...
    def __add__(self, other: Input) -> Double: ...
    def __sub__(self, other: Input) -> Double: ...
    def __mul__(self, other: Input) -> Double: ...
    def __floordiv__(self, other: Input) -> Double: ...
    def __truediv__(self, other: Input) -> Double: ...
    def __mod__(self, other: Input) -> Double: ...
    def __pow__(self, other: Input) -> Double: ...
    def __iadd__(self, other: Input) -> Double: ...
    def __isub__(self, other: Input) -> Double: ...
    def __imul__(self, other: Input) -> Double: ...
    def __idiv__(self, other: Input) -> Double: ...
    def __ifloordiv__(self, other: Input) -> Double: ...
    def __itruediv__(self, other: Input) -> Double: ...
    def __imod__(self, other: Input) -> Double: ...

class PDouble(DoubleBase):
    def __init__(self, value: Double) -> None: ...
    def setvalue(self, value: Input) -> None: ...
    def __getitem__(self, key: int) -> float: ...
    def __setitem__(self, key: int, value: Input) -> None: ...
    def __add__(self, other: Input) -> Double: ...
    def __sub__(self, other: Input) -> Double: ...
    def __mul__(self, other: Input) -> Double: ...
    def __floordiv__(self, other: Input) -> Double: ...
    def __truediv__(self, other: Input) -> Double: ...
    def __mod__(self, other: Input) -> Double: ...
    def __pow__(self, other: Input) -> Double: ...
    def __iadd__(self, other: Input) -> PDouble: ...
    def __isub__(self, other: Input) -> PDouble: ...
    def __imul__(self, other: Input) -> PDouble: ...
    def __idiv__(self, other: Input) -> PDouble: ...
    def __ifloordiv__(self, other: Input) -> PDouble: ...
    def __itruediv__(self, other: Input) -> PDouble: ...
    def __imod__(self, other: Input) -> PDouble: ...

class PPDouble:
    def __init__(self) -> None: ...
    def set_pointer(self, value: Double, idx: int) -> None: ...
    def _prepare_indices(self, idxs: Union[int, slice]) -> List[int]: ...
    def __getitem__(self, key: Union[int, slice]) -> typingtools.Vector[float]: ...
    def __setitem__(
        self, key: Union[int, slice], value: typingtools.VectorInput[float]
    ) -> None: ...
    def _get_shape(self) -> Tuple[int]: ...
    def _set_shape(self, length: int) -> None: ...
    shape = property(_get_shape, _set_shape)

def check0(length: int) -> None: ...
def check1(length: int, idx: int) -> None: ...
def check2(ready: typingtools.VectorInput[float], length: int) -> None: ...
