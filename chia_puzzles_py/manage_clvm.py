import io

from clvm.serialize import sexp_from_stream
from clvm_tools.sha256tree import sha256tree
from clvm import to_sexp_f

def generate_hash_bytes(clvm_bytes: bytes) -> bytes:
    serialized_hash = sha256tree(sexp_from_stream(io.BytesIO(clvm_bytes), to_sexp_f))
    return serialized_hash
