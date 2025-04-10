#!/usr/bin/env python3
"""
example_keys.py

Demonstrates how to generate Ed25519/ECDSA private keys,
convert them to/from raw and DER encodings, and sign/verify messages
using the new explicit loaders in the hiero_sdk_python.crypto module.
"""

from hiero_sdk_python.crypto.private_key import PrivateKey
from hiero_sdk_python.crypto.public_key import PublicKey


def example_ed25519_raw():
    print("=== Ed25519 (Raw) ===")
    # Generate Ed25519 private key
    priv_ed = PrivateKey.generate_ed25519()
    print("Ed25519 Private Key (raw hex):", priv_ed.to_string_raw())

    # Derive the public key
    pub_ed = priv_ed.public_key()
    print("Ed25519 Public Key (raw hex):", pub_ed.to_string_raw())

    # Reload the private key from its raw hex
    priv_ed_loaded = PrivateKey.from_string_ed25519(priv_ed.to_string_raw())
    # Reload the public key from its raw hex
    pub_ed_loaded = PublicKey.from_string_ed25519(pub_ed.to_string_raw())

    # Sign and verify
    message = b"Hello, Ed25519!"
    signature = priv_ed.sign(message)
    try:
        pub_ed.verify(signature, message)
        print("Ed25519 signature verified successfully.")
    except Exception as e:
        print("Ed25519 signature verification failed:", e)

    # Sanity checks
    print("Private keys match?" , priv_ed_loaded.to_string_raw() == priv_ed.to_string_raw())
    print("Public keys match?"  , pub_ed_loaded.to_string_raw()  == pub_ed.to_string_raw())
    print()


def example_ed25519_der():
    print("=== Ed25519 (DER) ===")
    # Generate Ed25519 private key
    priv_ed = PrivateKey.generate_ed25519()
    print("Ed25519 Private Key (DER hex):", priv_ed.to_string_der())

    # Derive the public key and show DER
    pub_ed = priv_ed.public_key()
    print("Ed25519 Public Key (DER hex):", pub_ed.to_string_der())

    # Reload the private key from DER hex
    priv_ed_loaded = PrivateKey.from_string_der(priv_ed.to_string_der())
    # Reload the public key from DER hex
    pub_ed_loaded = PublicKey.from_string_der(pub_ed.to_string_der())

    # Sign and verify
    message = b"Hello, Ed25519 in DER!"
    signature = priv_ed.sign(message)
    try:
        pub_ed.verify(signature, message)
        print("DER-based Ed25519 signature verified successfully.")
    except Exception as e:
        print("DER-based Ed25519 signature verification failed:", e)

    # Sanity checks
    print("Private keys match?" , priv_ed_loaded.to_string_der() == priv_ed.to_string_der())
    print("Public keys match?"  , pub_ed_loaded.to_string_der()  == pub_ed.to_string_der())
    print()


def example_ecdsa_raw():
    print("=== ECDSA (Raw) ===")
    # Generate ECDSA private key
    priv_ecdsa = PrivateKey.generate_ecdsa()
    print("ECDSA Private Key (raw hex):", priv_ecdsa.to_string_raw())

    # Derive the public key
    pub_ecdsa = priv_ecdsa.public_key()
    print("ECDSA Public Key (raw hex):", pub_ecdsa.to_string_raw())

    # Reload the private key from raw hex
    priv_ecdsa_loaded = PrivateKey.from_string_ecdsa(priv_ecdsa.to_string_raw())
    # Reload the public key from raw hex
    pub_ecdsa_loaded = PublicKey.from_string_ecdsa(pub_ecdsa.to_string_raw())

    # Sign and verify
    message = b"Hello, ECDSA!"
    signature = priv_ecdsa.sign(message)
    try:
        pub_ecdsa.verify(signature, message)
        print("ECDSA signature verified successfully.")
    except Exception as e:
        print("ECDSA signature verification failed:", e)

    # Sanity checks
    print("Private keys match?" , priv_ecdsa_loaded.to_string_raw() == priv_ecdsa.to_string_raw())
    print("Public keys match?"  , pub_ecdsa_loaded.to_string_raw()  == pub_ecdsa.to_string_raw())
    print()


def example_ecdsa_der():
    print("=== ECDSA (DER) ===")
    # Generate ECDSA private key
    priv_ecdsa = PrivateKey.generate_ecdsa()
    print("ECDSA Private Key (DER hex):", priv_ecdsa.to_string_der())

    # Derive the public key and show DER
    pub_ecdsa = priv_ecdsa.public_key()
    print("ECDSA Public Key (DER hex):", pub_ecdsa.to_string_der())

    # Reload the private key from DER hex
    priv_ecdsa_loaded = PrivateKey.from_string_der(priv_ecdsa.to_string_der())
    # Reload the public key from DER hex
    pub_ecdsa_loaded = PublicKey.from_string_der(pub_ecdsa.to_string_der())

    # Sign and verify
    message = b"Hello, ECDSA in DER!"
    signature = priv_ecdsa.sign(message)
    try:
        pub_ecdsa.verify(signature, message)
        print("DER-based ECDSA signature verified successfully.")
    except Exception as e:
        print("DER-based ECDSA signature verification failed:", e)

    # Sanity checks
    print("Private keys match?" , priv_ecdsa_loaded.to_string_der() == priv_ecdsa.to_string_der())
    print("Public keys match?"  , pub_ecdsa_loaded.to_string_der()  == pub_ecdsa.to_string_der())
    print()


def main():
    example_ed25519_raw()
    example_ed25519_der()
    example_ecdsa_raw()
    example_ecdsa_der()


if __name__ == "__main__":
    main()
