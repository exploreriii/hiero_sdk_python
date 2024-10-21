import pytest
from unittest.mock import MagicMock
from src.tokens.token_create_transaction import TokenCreateTransaction
from src.outputs import basic_types_pb2, timestamp_pb2

def generate_transaction_id(account_id_proto):
    """Generate a unique transaction ID based on the account ID and the current timestamp."""
    import time
    current_time = time.time()
    timestamp_seconds = int(current_time)
    timestamp_nanos = int((current_time - timestamp_seconds) * 1e9)

    tx_timestamp = timestamp_pb2.Timestamp(seconds=timestamp_seconds, nanos=timestamp_nanos)

    tx_id = basic_types_pb2.TransactionID(
        transactionValidStart=tx_timestamp,
        accountID=account_id_proto
    )
    return tx_id

def test_build_transaction_body(mock_account_ids):
    """Test building a token creation transaction body with valid values."""
    treasury_account, _, node_account_id, _, _ = mock_account_ids

    token_tx = TokenCreateTransaction()
    token_tx.set_token_name("MyToken")
    token_tx.set_token_symbol("MTK")
    token_tx.set_decimals(2)
    token_tx.set_initial_supply(1000)
    token_tx.set_treasury_account_id(treasury_account)
    token_tx.transaction_id = generate_transaction_id(treasury_account.to_proto())
    token_tx.node_account_id = node_account_id

    transaction_body = token_tx.build_transaction_body()

    assert transaction_body.tokenCreation.name == "MyToken"
    assert transaction_body.tokenCreation.symbol == "MTK"
    assert transaction_body.tokenCreation.decimals == 2
    assert transaction_body.tokenCreation.initialSupply == 1000

def test_missing_fields():
    """Test that building a transaction without required fields raises a ValueError."""
    token_tx = TokenCreateTransaction()
    with pytest.raises(ValueError, match="Missing required fields"):
        token_tx.build_transaction_body()

def test_sign_transaction(mock_account_ids):
    """Test signing the token creation transaction with a private key."""
    treasury_account, _, node_account_id, _, _ = mock_account_ids
    token_tx = TokenCreateTransaction()
    token_tx.set_token_name("MyToken")
    token_tx.set_token_symbol("MTK")
    token_tx.set_decimals(2)
    token_tx.set_initial_supply(1000)
    token_tx.set_treasury_account_id(treasury_account)
    token_tx.transaction_id = generate_transaction_id(treasury_account.to_proto())
    token_tx.node_account_id = node_account_id

    private_key = MagicMock()
    private_key.sign.return_value = b'signature'
    private_key.public_key().public_bytes.return_value = b'public_key'

    token_tx.sign(private_key)

    assert len(token_tx.signature_map.sigPair) == 1
    sig_pair = token_tx.signature_map.sigPair[0]
    assert sig_pair.pubKeyPrefix == b'public_key' 
    assert sig_pair.ed25519 == b'signature'


def test_to_proto(mock_account_ids):
    """Test converting the token creation transaction to protobuf format after signing."""
    treasury_account, _, node_account_id, _, _ = mock_account_ids
    token_tx = TokenCreateTransaction()
    token_tx.set_token_name("MyToken")
    token_tx.set_token_symbol("MTK")
    token_tx.set_decimals(2)
    token_tx.set_initial_supply(1000)
    token_tx.set_treasury_account_id(treasury_account)
    token_tx.transaction_id = generate_transaction_id(treasury_account.to_proto())
    token_tx.node_account_id = node_account_id

    private_key = MagicMock()
    private_key.sign.return_value = b'signature'
    private_key.public_key().public_bytes.return_value = b'public_key'

    token_tx.sign(private_key)
    proto = token_tx.to_proto()

    assert proto.signedTransactionBytes
    assert len(proto.signedTransactionBytes) > 0
