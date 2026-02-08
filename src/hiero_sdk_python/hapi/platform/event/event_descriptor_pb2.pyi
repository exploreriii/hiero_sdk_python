from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EventDescriptor(_message.Message):
    __slots__ = ("hash", "creator_node_id", "birth_round", "generation")
    HASH_FIELD_NUMBER: _ClassVar[int]
    CREATOR_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    BIRTH_ROUND_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    hash: bytes
    creator_node_id: int
    birth_round: int
    generation: int
    def __init__(self, hash: _Optional[bytes] = ..., creator_node_id: _Optional[int] = ..., birth_round: _Optional[int] = ..., generation: _Optional[int] = ...) -> None: ...
