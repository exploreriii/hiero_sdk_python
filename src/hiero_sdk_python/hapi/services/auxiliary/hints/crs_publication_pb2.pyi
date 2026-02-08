from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CrsPublicationTransactionBody(_message.Message):
    __slots__ = ("new_crs", "proof")
    NEW_CRS_FIELD_NUMBER: _ClassVar[int]
    PROOF_FIELD_NUMBER: _ClassVar[int]
    new_crs: bytes
    proof: bytes
    def __init__(self, new_crs: _Optional[bytes] = ..., proof: _Optional[bytes] = ...) -> None: ...
