# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: file_update.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'file_update.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import basic_types_pb2 as basic__types__pb2
from . import timestamp_pb2 as timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x66ile_update.proto\x12\x05proto\x1a\x11\x62\x61sic_types.proto\x1a\x0ftimestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xc0\x01\n\x19\x46ileUpdateTransactionBody\x12\x1d\n\x06\x66ileID\x18\x01 \x01(\x0b\x32\r.proto.FileID\x12(\n\x0e\x65xpirationTime\x18\x02 \x01(\x0b\x32\x10.proto.Timestamp\x12\x1c\n\x04keys\x18\x03 \x01(\x0b\x32\x0e.proto.KeyList\x12\x10\n\x08\x63ontents\x18\x04 \x01(\x0c\x12*\n\x04memo\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValueB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'file_update_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.hederahashgraph.api.proto.javaP\001'
  _globals['_FILEUPDATETRANSACTIONBODY']._serialized_start=97
  _globals['_FILEUPDATETRANSACTIONBODY']._serialized_end=289
# @@protoc_insertion_point(module_scope)
