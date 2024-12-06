import hashlib
import typing

from clvm.CLVMObject import CLVMStorage
from clvm.SExp import SExp

ValueType = typing.Union[bytes, CLVMStorage]
ValueStackType = typing.List[ValueType]
Op = typing.Callable[[ValueStackType, "OpStackType", typing.Set[bytes]], None]
OpStackType = typing.List[Op]

def std_hash(
    b: typing.Union[bytes, typing.SupportsBytes], skip_bytes_conversion: bool = False
) -> bytes:
    """
    The standard hash used in many places.
    """
    if skip_bytes_conversion:
        # casting for hinting based on above overloads constraining the type
        return hashlib.sha256(typing.cast(bytes, b)).digest()
    else:
        return hashlib.sha256(bytes(b)).digest()

def generate_hash_bytes(clvm_bytes: bytes) -> bytes:
    serialized_hash = sha256_treehash(SExp.to(clvm_bytes))
    return serialized_hash

def sha256_treehash(
    sexp: CLVMStorage, precalculated: typing.Optional[typing.Set[bytes]] = None
) -> bytes:
    """
    Hash values in `precalculated` are presumed to have been hashed already.
    """

    if precalculated is None:
        precalculated = set()

    def handle_sexp(
        sexp_stack: ValueStackType,
        op_stack: OpStackType,
        precalculated: typing.Set[bytes],
    ) -> None:
        # just trusting it is right, otherwise we get an attribute error
        sexp: SExp = sexp_stack.pop()  # type: ignore[assignment]
        if sexp.pair:
            p0, p1 = sexp.pair
            sexp_stack.append(p0)
            sexp_stack.append(p1)
            op_stack.append(handle_pair)
            op_stack.append(handle_sexp)
            op_stack.append(roll)
            op_stack.append(handle_sexp)
        else:
            # not a pair, so an atom
            atom: bytes = sexp.atom  # type: ignore[assignment]
            if atom in precalculated:
                r = atom
            else:
                r = std_hash(b"\1" + atom)
            sexp_stack.append(r)

    def handle_pair(
        sexp_stack: ValueStackType,
        op_stack: OpStackType,
        precalculated: typing.Set[bytes],
    ) -> None:
        # just trusting it is right, otherwise we get a type error
        p0: bytes = sexp_stack.pop()  # type: ignore[assignment]
        p1: bytes = sexp_stack.pop()  # type: ignore[assignment]
        sexp_stack.append(std_hash(b"\2" + p0 + p1))

    def roll(
        sexp_stack: ValueStackType,
        op_stack: OpStackType,
        precalculated: typing.Set[bytes],
    ) -> None:
        p0 = sexp_stack.pop()
        p1 = sexp_stack.pop()
        sexp_stack.append(p0)
        sexp_stack.append(p1)

    sexp_stack: ValueStackType = [sexp]
    op_stack: typing.List[Op] = [handle_sexp]
    while len(op_stack) > 0:
        op = op_stack.pop()
        op(sexp_stack, op_stack, precalculated)

    result: bytes = sexp_stack[0]  # type: ignore[assignment]
    return result