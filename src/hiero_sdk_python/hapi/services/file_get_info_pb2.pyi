from . import timestamp_pb2 as _timestamp_pb2
from . import basic_types_pb2 as _basic_types_pb2
from . import query_header_pb2 as _query_header_pb2
from . import response_header_pb2 as _response_header_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileGetInfoQuery(_message.Message):
    __slots__ = ("header", "fileID")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    FILEID_FIELD_NUMBER: _ClassVar[int]
    header: _query_header_pb2.QueryHeader
    fileID: _basic_types_pb2.FileID
    def __init__(self, header: _Optional[_Union[_query_header_pb2.QueryHeader, _Mapping]] = ..., fileID: _Optional[_Union[_basic_types_pb2.FileID, _Mapping]] = ...) -> None: ...

class FileGetInfoResponse(_message.Message):
    __slots__ = ("header", "fileInfo")
    class FileInfo(_message.Message):
        __slots__ = ("fileID", "size", "expirationTime", "deleted", "keys", "memo", "ledger_id")
        FILEID_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        EXPIRATIONTIME_FIELD_NUMBER: _ClassVar[int]
        DELETED_FIELD_NUMBER: _ClassVar[int]
        KEYS_FIELD_NUMBER: _ClassVar[int]
        MEMO_FIELD_NUMBER: _ClassVar[int]
        LEDGER_ID_FIELD_NUMBER: _ClassVar[int]
        fileID: _basic_types_pb2.FileID
        size: int
        expirationTime: _timestamp_pb2.Timestamp
        deleted: bool
        keys: _basic_types_pb2.KeyList
        memo: str
        ledger_id: bytes
        def __init__(self, fileID: _Optional[_Union[_basic_types_pb2.FileID, _Mapping]] = ..., size: _Optional[int] = ..., expirationTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted: bool = ..., keys: _Optional[_Union[_basic_types_pb2.KeyList, _Mapping]] = ..., memo: _Optional[str] = ..., ledger_id: _Optional[bytes] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    FILEINFO_FIELD_NUMBER: _ClassVar[int]
    header: _response_header_pb2.ResponseHeader
    fileInfo: FileGetInfoResponse.FileInfo
    def __init__(self, header: _Optional[_Union[_response_header_pb2.ResponseHeader, _Mapping]] = ..., fileInfo: _Optional[_Union[FileGetInfoResponse.FileInfo, _Mapping]] = ...) -> None: ...
