"""
pause_token.py

This script demonstrates how to pause an existing token.

It:
1. Loads environment variables for operator and pause key
2. Sets up a client
3. Pauses the token specified by TOKEN_ID
4. Prints the result or error

Required environment variables:
- OPERATOR_ID, OPERATOR_KEY (mandatory)
- TOKEN_ID (the ID of the token to pause)
- PAUSE_KEY (the key authorized to pause this token)

Dependencies:
- dotenv
- hiero_sdk_python
"""

import os
import sys
from dotenv import load_dotenv

# Hiero SDK imports
from hiero_sdk_python.client.network import Network
from hiero_sdk_python.client.client import Client
from hiero_sdk_python.account.account_id import AccountId
from hiero_sdk_python.crypto.private_key import PrivateKey
from hiero_sdk_python.tokens.token_id import TokenId
from hiero_sdk_python.tokens.token_pause_transaction import TokenPauseTransaction
from hiero_sdk_python.response_code import ResponseCode

load_dotenv()


def pause_token():
    """Function to pause a token."""

    # Network Setup
    network = Network(network='testnet')
    client = Client(network)

    # Operator credentials (must be present)
    operator_id = AccountId.from_string(os.getenv('OPERATOR_ID'))
    operator_key = PrivateKey.from_string(os.getenv('OPERATOR_KEY'))

    # Required Pause Key
    pause_key = PrivateKey.from_string(os.getenv('PAUSE_KEY')) # Optional

    # Set the operator for the client
    client.set_operator(operator_id, operator_key)

    # Create the token pause transaction
    transaction = TokenPauseTransaction(token_id=token_id)

    transaction.freeze_with(client)

    # The operator (fee payer) signs first
    transaction.sign(operator_key)

    # The pause key must sign
    transaction.sign(pause_key)

    try:

        # Execute the transaction and get the receipt
        receipt = transaction.execute(client)

        if receipt and receipt.tokenId:
            print(f"Token paused with ID: {receipt.tokenId}")
        else:
            print("Token paused failed: Token ID not returned in receipt.")
            sys.exit(1)

    except Exception as e:
        print(f"Token paused failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    pause_token()