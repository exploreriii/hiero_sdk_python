from . import state_signature_transaction_pb2 as _state_signature_transaction_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransactionGroupRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STANDALONE: _ClassVar[TransactionGroupRole]
    FIRST_CHILD: _ClassVar[TransactionGroupRole]
    MIDDLE_CHILD: _ClassVar[TransactionGroupRole]
    LAST_CHILD: _ClassVar[TransactionGroupRole]
    STARTING_PARENT: _ClassVar[TransactionGroupRole]
    PARENT: _ClassVar[TransactionGroupRole]
    ENDING_PARENT: _ClassVar[TransactionGroupRole]
STANDALONE: TransactionGroupRole
FIRST_CHILD: TransactionGroupRole
MIDDLE_CHILD: TransactionGroupRole
LAST_CHILD: TransactionGroupRole
STARTING_PARENT: TransactionGroupRole
PARENT: TransactionGroupRole
ENDING_PARENT: TransactionGroupRole

class EventTransaction(_message.Message):
    __slots__ = ("application_transaction", "state_signature_transaction", "transaction_group_role")
    APPLICATION_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    STATE_SIGNATURE_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_GROUP_ROLE_FIELD_NUMBER: _ClassVar[int]
    application_transaction: bytes
    state_signature_transaction: _state_signature_transaction_pb2.StateSignatureTransaction
    transaction_group_role: TransactionGroupRole
    def __init__(self, application_transaction: _Optional[bytes] = ..., state_signature_transaction: _Optional[_Union[_state_signature_transaction_pb2.StateSignatureTransaction, _Mapping]] = ..., transaction_group_role: _Optional[_Union[TransactionGroupRole, str]] = ...) -> None: ...
