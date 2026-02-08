from . import basic_types_pb2 as _basic_types_pb2
from . import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileUpdateTransactionBody(_message.Message):
    __slots__ = ("fileID", "expirationTime", "keys", "contents", "memo")
    FILEID_FIELD_NUMBER: _ClassVar[int]
    EXPIRATIONTIME_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    fileID: _basic_types_pb2.FileID
    expirationTime: _timestamp_pb2.Timestamp
    keys: _basic_types_pb2.KeyList
    contents: bytes
    memo: _wrappers_pb2.StringValue
    def __init__(self, fileID: _Optional[_Union[_basic_types_pb2.FileID, _Mapping]] = ..., expirationTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., keys: _Optional[_Union[_basic_types_pb2.KeyList, _Mapping]] = ..., contents: _Optional[bytes] = ..., memo: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...
