# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: system_undelete.proto
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
    'system_undelete.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import basic_types_pb2 as basic__types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15system_undelete.proto\x12\x05proto\x1a\x11\x62\x61sic_types.proto\"o\n\x1dSystemUndeleteTransactionBody\x12\x1f\n\x06\x66ileID\x18\x01 \x01(\x0b\x32\r.proto.FileIDH\x00\x12\'\n\ncontractID\x18\x02 \x01(\x0b\x32\x11.proto.ContractIDH\x00\x42\x04\n\x02idB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'system_undelete_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.hederahashgraph.api.proto.javaP\001'
  _globals['_SYSTEMUNDELETETRANSACTIONBODY']._serialized_start=51
  _globals['_SYSTEMUNDELETETRANSACTIONBODY']._serialized_end=162
# @@protoc_insertion_point(module_scope)
