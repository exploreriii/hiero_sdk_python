"""
test_keys.py

A comprehensive test suite for the new hierarchical crypto system:
- Tests Ed25519 & ECDSA private/public key generation
- Verifies trips from raw and DER encodings
- Validates correct error handling for invalid inputs
- Demonstrates sign & verify
"""

import pytest
from hiero_sdk_python.crypto.private_key import PrivateKey
from hiero_sdk_python.crypto.public_key import PublicKey
from cryptography.exceptions import InvalidSignature

def test_ed25519_private_key_raw_roundtrip():
    """Generate an Ed25519 private key, export to raw hex, reload, compare."""
    priv = PrivateKey.generate_ed25519()
    raw_hex = priv.to_string_raw()
    reloaded = PrivateKey.from_string_ed25519(raw_hex)
    assert reloaded.to_string_raw() == raw_hex, "Ed25519 private key raw round-trip failed."

def test_ed25519_public_key_raw_roundtrip():
    """Derive Ed25519 public key, export to raw hex, reload, compare."""
    priv = PrivateKey.generate_ed25519()
    pub = priv.public_key()
    raw_hex = pub.to_string_raw()
    reloaded = PublicKey.from_string_ed25519(raw_hex)
    assert reloaded.to_string_raw() == raw_hex, "Ed25519 public key raw round-trip failed."

def test_ecdsa_private_key_raw_roundtrip():
    """Generate an ECDSA private key, export to raw hex, reload, compare."""
    priv = PrivateKey.generate_ecdsa()
    raw_hex = priv.to_string_raw()
    reloaded = PrivateKey.from_string_ecdsa(raw_hex)
    assert reloaded.to_string_raw() == raw_hex, "ECDSA private key raw round-trip failed."

def test_ecdsa_public_key_raw_roundtrip():
    """Derive ECDSA public key, export to raw hex, reload, compare."""
    priv = PrivateKey.generate_ecdsa()
    pub = priv.public_key()
    raw_hex = pub.to_string_raw()
    reloaded = PublicKey.from_string_ecdsa(raw_hex)
    assert reloaded.to_string_raw() == raw_hex, "ECDSA public key raw round-trip failed."

def test_ed25519_private_key_der_roundtrip():
    """Generate an Ed25519 private key, export to DER, reload, compare."""
    priv = PrivateKey.generate_ed25519()
    der_hex = priv.to_string_der()
    reloaded = PrivateKey.from_string_der(der_hex)
    assert reloaded.to_string_der() == der_hex, "Ed25519 private key DER round-trip failed."

def test_ed25519_public_key_der_roundtrip():
    """Derive Ed25519 public key, export to DER, reload, compare."""
    priv = PrivateKey.generate_ed25519()
    pub = priv.public_key()
    der_hex = pub.to_string_der()
    reloaded = PublicKey.from_string_der(der_hex)
    assert reloaded.to_string_der() == der_hex, "Ed25519 public key DER round-trip failed."

def test_ecdsa_private_key_der_roundtrip():
    """Generate ECDSA private key, export to DER, reload, compare."""
    priv = PrivateKey.generate_ecdsa()
    der_hex = priv.to_string_der()
    reloaded = PrivateKey.from_string_der(der_hex)
    assert reloaded.to_string_der() == der_hex, "ECDSA private key DER round-trip failed."

def test_ecdsa_public_key_der_roundtrip():
    """Derive ECDSA public key, export to DER, reload, compare."""
    priv = PrivateKey.generate_ecdsa()
    pub = priv.public_key()
    der_hex = pub.to_string_der()
    reloaded = PublicKey.from_string_der(der_hex)
    assert reloaded.to_string_der() == der_hex, "ECDSA public key DER round-trip failed."

def test_sign_verify_ed25519():
    """Test Ed25519 signing and verifying."""
    priv = PrivateKey.generate_ed25519()
    pub = priv.public_key()
    message = b"Hello Ed25519!"
    signature = priv.sign(message)
    # Should not raise an exception
    pub.verify(signature, message)

    # Try verifying wrong message => should raise an exception
    with pytest.raises(InvalidSignature):
        pub.verify(signature, b"Wrong message")

def test_sign_verify_ecdsa():
    """Test ECDSA signing and verifying."""
    priv = PrivateKey.generate_ecdsa()
    pub = priv.public_key()
    message = b"Hello ECDSA!"
    signature = priv.sign(message)
    # Should not raise an exception
    pub.verify(signature, message)

    with pytest.raises(InvalidSignature):
        pub.verify(signature, b"Bad message")

def test_invalid_ed25519_seed_length():
    """Ensure loading an Ed25519 key with invalid length raises ValueError."""
    # Each byte is 2 hex chars, so 64 hex chars = 32 bytes
    # Here we only do 10 bytes worth (20 hex chars).
    short_hex = "a0" * 10
    with pytest.raises(ValueError):
        PrivateKey.from_string_ed25519(short_hex)

def test_invalid_ecdsa_seed_length():
    """Ensure loading an ECDSA key with invalid length raises ValueError."""
    # ECDSA private scalar should be 32 bytes => 64 hex chars
    short_hex = "ff" * 10
    with pytest.raises(ValueError):
        PrivateKey.from_string_ecdsa(short_hex)

def test_invalid_public_key_length():
    """Ensure loading an Ed25519 public key with invalid length raises ValueError."""
    short_hex = "ab" * 10  # only 20 hex chars => 10 bytes
    with pytest.raises(ValueError):
        PublicKey.from_string_ed25519(short_hex)
