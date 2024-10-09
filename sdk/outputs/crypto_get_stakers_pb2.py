# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: crypto_get_stakers.proto
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
    'crypto_get_stakers.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import basic_types_pb2 as basic__types__pb2
from . import query_header_pb2 as query__header__pb2
from . import response_header_pb2 as response__header__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x63rypto_get_stakers.proto\x12\x05proto\x1a\x11\x62\x61sic_types.proto\x1a\x12query_header.proto\x1a\x15response_header.proto\"`\n\x15\x43ryptoGetStakersQuery\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.proto.QueryHeader\x12#\n\taccountID\x18\x02 \x01(\x0b\x32\x10.proto.AccountID\"B\n\x0bProxyStaker\x12#\n\taccountID\x18\x01 \x01(\x0b\x32\x10.proto.AccountID\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\"_\n\x0f\x41llProxyStakers\x12#\n\taccountID\x18\x01 \x01(\x0b\x32\x10.proto.AccountID\x12\'\n\x0bproxyStaker\x18\x02 \x03(\x0b\x32\x12.proto.ProxyStaker\"j\n\x18\x43ryptoGetStakersResponse\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.proto.ResponseHeader\x12\'\n\x07stakers\x18\x03 \x01(\x0b\x32\x16.proto.AllProxyStakersB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'crypto_get_stakers_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.hederahashgraph.api.proto.javaP\001'
  _globals['_CRYPTOGETSTAKERSQUERY']._serialized_start=97
  _globals['_CRYPTOGETSTAKERSQUERY']._serialized_end=193
  _globals['_PROXYSTAKER']._serialized_start=195
  _globals['_PROXYSTAKER']._serialized_end=261
  _globals['_ALLPROXYSTAKERS']._serialized_start=263
  _globals['_ALLPROXYSTAKERS']._serialized_end=358
  _globals['_CRYPTOGETSTAKERSRESPONSE']._serialized_start=360
  _globals['_CRYPTOGETSTAKERSRESPONSE']._serialized_end=466
# @@protoc_insertion_point(module_scope)
