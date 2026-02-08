from . import basic_types_pb2 as _basic_types_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileAppendTransactionBody(_message.Message):
    __slots__ = ("fileID", "contents")
    FILEID_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    fileID: _basic_types_pb2.FileID
    contents: bytes
    def __init__(self, fileID: _Optional[_Union[_basic_types_pb2.FileID, _Mapping]] = ..., contents: _Optional[bytes] = ...) -> None: ...
