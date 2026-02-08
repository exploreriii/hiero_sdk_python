from . import basic_types_pb2 as _basic_types_pb2
from . import query_header_pb2 as _query_header_pb2
from . import response_header_pb2 as _response_header_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileGetContentsQuery(_message.Message):
    __slots__ = ("header", "fileID")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    FILEID_FIELD_NUMBER: _ClassVar[int]
    header: _query_header_pb2.QueryHeader
    fileID: _basic_types_pb2.FileID
    def __init__(self, header: _Optional[_Union[_query_header_pb2.QueryHeader, _Mapping]] = ..., fileID: _Optional[_Union[_basic_types_pb2.FileID, _Mapping]] = ...) -> None: ...

class FileGetContentsResponse(_message.Message):
    __slots__ = ("header", "fileContents")
    class FileContents(_message.Message):
        __slots__ = ("fileID", "contents")
        FILEID_FIELD_NUMBER: _ClassVar[int]
        CONTENTS_FIELD_NUMBER: _ClassVar[int]
        fileID: _basic_types_pb2.FileID
        contents: bytes
        def __init__(self, fileID: _Optional[_Union[_basic_types_pb2.FileID, _Mapping]] = ..., contents: _Optional[bytes] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    FILECONTENTS_FIELD_NUMBER: _ClassVar[int]
    header: _response_header_pb2.ResponseHeader
    fileContents: FileGetContentsResponse.FileContents
    def __init__(self, header: _Optional[_Union[_response_header_pb2.ResponseHeader, _Mapping]] = ..., fileContents: _Optional[_Union[FileGetContentsResponse.FileContents, _Mapping]] = ...) -> None: ...
