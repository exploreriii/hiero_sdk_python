import pytest
import re
from unittest.mock import MagicMock, patch

from hiero_sdk_python.response_code import ResponseCode
from hiero_sdk_python.tokens.token_pause_transaction import TokenPauseTransaction
from hiero_sdk_python.hapi.services import timestamp_pb2
from hiero_sdk_python.transaction.transaction_id import TransactionId
from hiero_sdk_python.transaction.transaction import Transaction

def generate_transaction_id(account_id_proto):
    """Generate a unique transaction ID based on the account ID and the current timestamp."""
    import time
    current_time = time.time()
    timestamp_seconds = int(current_time)
    timestamp_nanos = int((current_time - timestamp_seconds) * 1e9)

    tx_timestamp = timestamp_pb2.Timestamp(seconds=timestamp_seconds, nanos=timestamp_nanos)

    tx_id = TransactionId(valid_start=tx_timestamp, account_id=account_id_proto)
    return tx_id

def test_build_transaction_body(mock_account_ids):
    """Test building a token pause transaction body with a valid token_id."""
    account_id, _, node_account_id, token_id, _ = mock_account_ids

    pause_tx = TokenPauseTransaction()
    pause_tx.set_token_id(token_id)

    pause_tx.transaction_id = generate_transaction_id(account_id)
    pause_tx.node_account_id = node_account_id

    transaction_body = pause_tx.build_transaction_body()

    assert transaction_body.token_pause.token.shardNum == token_id.shard
    assert transaction_body.token_pause.token.realmNum == token_id.realm
    assert transaction_body.token_pause.token.tokenNum == token_id.num

def test_missing_token_id(mock_account_ids):
    """Test that building a token pause transaction without setting a TokenID raises a ValueError."""
    account_id, _, node_account_id, _, _ = mock_account_ids

    pause_tx = TokenPauseTransaction()

    pause_tx.transaction_id = generate_transaction_id(account_id)
    pause_tx.node_account_id = node_account_id

    with pytest.raises(ValueError, match="Token ID is required for pausing a token."):
        pause_tx.build_transaction_body()

def test_sign_transaction(mock_account_ids):
    """Test signing the token pause transaction with a pause key (or any valid key)."""
    account_id, _, node_account_id, token_id, _ = mock_account_ids

    pause_tx = TokenPauseTransaction()
    pause_tx.set_token_id(token_id)

    pause_tx.transaction_id = generate_transaction_id(account_id)
    pause_tx.node_account_id = node_account_id

    # Mock the pause key
    pause_key = MagicMock()
    pause_key.sign.return_value = b"pause_signature"
    pause_key.public_key().to_bytes_raw.return_value = b"pause_public_key"

    # Sign the transaction
    pause_tx.sign(pause_key)

    # Check that signature_map is updated
    assert len(pause_tx.signature_map.sigPair) == 1
    sig_pair = pause_tx.signature_map.sigPair[0]
    assert sig_pair.pubKeyPrefix == b"pause_public_key"
    assert sig_pair.ed25519 == b"pause_signature"

def test_already_paused_no_op(mock_account_ids):
    """
    Test that if the token is already paused, the transaction logs a message 
    but does not raise an error.
    """
    account_id, _, node_account_id, token_id, _ = mock_account_ids

    pause_tx = TokenPauseTransaction()
    pause_tx.set_token_id(token_id)

    pause_tx.transaction_id = generate_transaction_id(account_id)
    pause_tx.node_account_id = node_account_id

    # Mock client and token_info with paused=True
    mock_client = MagicMock()
    token_info = MagicMock()
    token_info.paused = True
    token_info.deleted = False
    token_info.pause_key = MagicMock()
    
    mock_client.get_token_info.return_value = token_info
    mock_client.token_stub.pauseToken.return_value.nodeTransactionPrecheckCode = ResponseCode.OK

    # Sign the transaction
    key = MagicMock()
    key.public_key().to_bytes_raw.return_value = b"pause_public_key"
    key.sign.return_value = b"pause_signature"
    pause_tx.sign(key)

    # Execute
    with patch('builtins.print') as mock_print:
        receipt = pause_tx._execute_transaction(mock_client, "mock_proto")
        # Confirm "Token is already paused." was printed
        mock_print.assert_any_call("Token is already paused.")

    # No error raised; transaction is effectively a no-op
    mock_client.token_stub.pauseToken.assert_called_once_with("mock_proto")

def test_deleted_token(mock_account_ids):
    """Test that an attempt to pause a deleted token raises ValueError."""
    account_id, _, node_account_id, token_id, _ = mock_account_ids

    pause_tx = TokenPauseTransaction()
    pause_tx.set_token_id(token_id)

    pause_tx.transaction_id = generate_transaction_id(account_id)
    pause_tx.node_account_id = node_account_id

    mock_client = MagicMock()
    token_info = MagicMock()
    token_info.deleted = True
    token_info.pause_key = MagicMock()
    mock_client.get_token_info.return_value = token_info

    with pytest.raises(ValueError, match="Cannot pause a deleted token."):
        pause_tx._execute_transaction(mock_client, "mock_proto")

def test_no_pause_key(mock_account_ids):
    """Test that an attempt to pause a token without a pause key raises ValueError."""
    account_id, _, node_account_id, token_id, _ = mock_account_ids

    pause_tx = TokenPauseTransaction()
    pause_tx.set_token_id(token_id)
    
    pause_tx.transaction_id = generate_transaction_id(account_id)
    pause_tx.node_account_id = node_account_id

    mock_client = MagicMock()
    token_info = MagicMock()
    token_info.deleted = False
    token_info.pause_key = None  # No pause key
    mock_client.get_token_info.return_value = token_info

    with pytest.raises(ValueError, match="Token has no valid pause key and cannot be paused."):
        pause_tx._execute_transaction(mock_client, "mock_proto")

def test_execute_transaction_success(mock_account_ids):
    """
    Test a successful pause transaction execution with nodeTransactionPrecheckCode == OK.
    """
    account_id, _, node_account_id, token_id, _ = mock_account_ids

    pause_tx = TokenPauseTransaction()
    pause_tx.set_token_id(token_id)
    pause_tx.transaction_id = generate_transaction_id(account_id)
    pause_tx.node_account_id = node_account_id

    # Mock client & token_info
    mock_client = MagicMock()
    token_info = MagicMock()
    token_info.deleted = False
    token_info.pause_key = MagicMock()
    token_info.paused = False
    mock_client.get_token_info.return_value = token_info

    # Stub returns OK
    mock_client.token_stub.pauseToken.return_value.nodeTransactionPrecheckCode = ResponseCode.OK

    # Execute
    receipt = pause_tx._execute_transaction(mock_client, "mock_proto")

    # Confirm the correct stub call
    mock_client.token_stub.pauseToken.assert_called_once_with("mock_proto")
    # Confirm we fetch a receipt
    mock_client.get_transaction_receipt.assert_called_once()
    # The returned receipt is whatever mock_client.get_receipt returns
    assert receipt == mock_client.get_transaction_receipt.return_value

def test_execute_transaction_failure(mock_account_ids):
    """
    Test that an exception is raised when token_pause transaction execution fails 
    (e.g., precheck code is INVALID_SIGNATURE).
    """
    account_id, _, node_account_id, token_id, _ = mock_account_ids

    pause_tx = TokenPauseTransaction()
    pause_tx.set_token_id(token_id)
    pause_tx.transaction_id = generate_transaction_id(account_id)
    pause_tx.node_account_id = node_account_id

    # Mock client
    mock_client = MagicMock()
    token_info = MagicMock()
    token_info.deleted = False
    token_info.pause_key = MagicMock()
    mock_client.get_token_info.return_value = token_info

    # Simulate an INVALID_SIGNATURE precheck
    mock_client.token_stub.pauseToken.return_value.nodeTransactionPrecheckCode = ResponseCode.INVALID_SIGNATURE
    
    expected_message = "Error during transaction submission: 7 (INVALID_SIGNATURE)"
    with pytest.raises(Exception, match=re.escape(expected_message)):
        pause_tx._execute_transaction(mock_client, "mock_proto")
    
    mock_client.token_stub.pauseToken.assert_called_once_with("mock_proto")
