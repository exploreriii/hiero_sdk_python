# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: throttle_definitions.proto
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
    'throttle_definitions.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import basic_types_pb2 as basic__types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1athrottle_definitions.proto\x12\x05proto\x1a\x11\x62\x61sic_types.proto\"W\n\rThrottleGroup\x12.\n\noperations\x18\x01 \x03(\x0e\x32\x1a.proto.HederaFunctionality\x12\x16\n\x0emilliOpsPerSec\x18\x02 \x01(\x04\"c\n\x0eThrottleBucket\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rburstPeriodMs\x18\x02 \x01(\x04\x12,\n\x0ethrottleGroups\x18\x03 \x03(\x0b\x32\x14.proto.ThrottleGroup\"E\n\x13ThrottleDefinitions\x12.\n\x0fthrottleBuckets\x18\x01 \x03(\x0b\x32\x15.proto.ThrottleBucketB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'throttle_definitions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.hederahashgraph.api.proto.javaP\001'
  _globals['_THROTTLEGROUP']._serialized_start=56
  _globals['_THROTTLEGROUP']._serialized_end=143
  _globals['_THROTTLEBUCKET']._serialized_start=145
  _globals['_THROTTLEBUCKET']._serialized_end=244
  _globals['_THROTTLEDEFINITIONS']._serialized_start=246
  _globals['_THROTTLEDEFINITIONS']._serialized_end=315
# @@protoc_insertion_point(module_scope)
