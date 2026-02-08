from . import basic_types_pb2 as _basic_types_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SignedTransaction(_message.Message):
    __slots__ = ("bodyBytes", "sigMap", "use_serialized_tx_message_hash_algorithm")
    BODYBYTES_FIELD_NUMBER: _ClassVar[int]
    SIGMAP_FIELD_NUMBER: _ClassVar[int]
    USE_SERIALIZED_TX_MESSAGE_HASH_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    bodyBytes: bytes
    sigMap: _basic_types_pb2.SignatureMap
    use_serialized_tx_message_hash_algorithm: bool
    def __init__(self, bodyBytes: _Optional[bytes] = ..., sigMap: _Optional[_Union[_basic_types_pb2.SignatureMap, _Mapping]] = ..., use_serialized_tx_message_hash_algorithm: bool = ...) -> None: ...
