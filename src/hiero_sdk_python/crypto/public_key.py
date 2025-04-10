import warnings
from cryptography.hazmat.primitives.asymmetric import ed25519, ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from typing import Union

class PublicKey:
    """
    Represents a public key that can be either Ed25519 or ECDSA (secp256k1).
    """

    def __init__(self, public_key: Union[ec.EllipticCurvePublicKey, ed25519.Ed25519PublicKey]):
        """
        Initializes a PublicKey from a cryptography PublicKey object.
        """
        self._public_key = public_key

    #
    # ---------------------------------
    # Type-specific 'from bytes' loaders
    # ---------------------------------
    #

    @classmethod
    def from_bytes_ed25519(cls, pub: bytes) -> "PublicKey":
        """
        Load an Ed25519 public key from 32 raw bytes.
        Raises ValueError if not exactly 32 bytes or invalid.
        """
        if len(pub) != 32:
            raise ValueError(f"Ed25519 public key must be 32 bytes, got {len(pub)}.")
        try:
            ed_pub = ed25519.Ed25519PublicKey.from_public_bytes(pub)
            return cls(ed_pub)
        except Exception as e:
            raise ValueError(f"Invalid Ed25519 public key bytes: {e}")

    @classmethod
    def from_bytes_ecdsa(cls, pub: bytes) -> "PublicKey":
        """
        Load an ECDSA secp256k1 public key from raw bytes (commonly 33 or 65 bytes).
        Raises ValueError if invalid or unsupported length.
        """
        if len(pub) not in (33, 65):
            raise ValueError(
                f"ECDSA (secp256k1) pubkey must be 33 or 65 bytes, got {len(pub)}."
            )
        try:
            ec_pub = ec.EllipticCurvePublicKey.from_encoded_point(ec.SECP256K1(), pub)
            return cls(ec_pub)
        except Exception as e:
            raise ValueError(f"Invalid ECDSA public key point: {e}")

    @classmethod
    def from_der(cls, der_bytes: bytes) -> "PublicKey":
        """
        Load a public key from DER encoding.
        Detects Ed25519 vs ECDSA(secp256k1). Raises ValueError if unsupported/invalid.
        """
        try:
            maybe_pub = serialization.load_der_public_key(der_bytes, backend=default_backend())
        except Exception as e:
            raise ValueError(f"Could not parse DER public key: {e}")

        # Check Ed25519
        if isinstance(maybe_pub, ed25519.Ed25519PublicKey):
            return cls(maybe_pub)

        # Check ECDSA
        if isinstance(maybe_pub, ec.EllipticCurvePublicKey):
            if not isinstance(maybe_pub.curve, ec.SECP256K1):
                raise ValueError("Only secp256k1 ECDSA is supported.")
            return cls(maybe_pub)

        raise ValueError("Unsupported public key type in DER (not Ed25519 or ECDSA).")

    #
    # -----------------------------------
    # Type-specific 'from string' loaders
    # -----------------------------------
    #

    @classmethod
    def from_string_ed25519(cls, hex_str: str) -> "PublicKey":
        """
        Interpret the given string as a hex-encoded 32-byte Ed25519 public key.
        """
        hex_str = hex_str.removeprefix("0x")
        try:
            pub = bytes.fromhex(hex_str)
        except ValueError:
            raise ValueError(f"Invalid hex string for Ed25519 public key: {hex_str}")
        return cls.from_bytes_ed25519(pub)

    @classmethod
    def from_string_ecdsa(cls, hex_str: str) -> "PublicKey":
        """
        Interpret the given string as a hex-encoded compressed/uncompressed ECDSA pubkey (33/65 bytes).
        """
        hex_str = hex_str.removeprefix("0x")
        try:
            pub = bytes.fromhex(hex_str)
        except ValueError:
            raise ValueError(f"Invalid hex string for ECDSA public key: {hex_str}")
        return cls.from_bytes_ecdsa(pub)

    @classmethod
    def from_string_der(cls, hex_str: str) -> "PublicKey":
        """
        Interpret the given string as hex-encoded DER bytes containing a public key.
        """
        hex_str = hex_str.removeprefix("0x")
        try:
            der_bytes = bytes.fromhex(hex_str)
        except ValueError:
            raise ValueError(f"Invalid hex string for DER public key: {hex_str}")
        return cls.from_der(der_bytes)

    #
    # ----------------------------
    # Others
    # ----------------------------
    #

    def verify(self, signature: bytes, data: bytes) -> None:
        """
        Verifies a signature for the given data using this public key.
        Raises an exception if the signature is invalid.

        Args:
            signature (bytes): The signature to verify.
            data (bytes): The data that was signed.

        Raises:
            cryptography.exceptions.InvalidSignature: If the signature is invalid.
        """
        if self.is_ed25519():
            self._public_key.verify(signature, data)
        else:
            # ECDSA requires specifying a hash algorithm
            from cryptography.hazmat.primitives.asymmetric import ec
            from cryptography.hazmat.primitives import hashes
            self._public_key.verify(signature, data, ec.ECDSA(hashes.SHA256()))

    def to_bytes_raw(self) -> bytes:
        """
        Returns the public key in raw form:
         - For Ed25519, it's 32 bytes.
         - For ECDSA (secp256k1), typically 33 bytes (compressed),
           depending on how cryptography outputs raw.

        Returns:
            bytes: The raw public key bytes.
        """
        if self.is_ed25519():
            return self._public_key.public_bytes(
                encoding=serialization.Encoding.Raw,
                format=serialization.PublicFormat.Raw
            )
        else:
            return self._public_key.public_bytes(
                encoding=serialization.Encoding.X962,
                format=serialization.PublicFormat.CompressedPoint
            )

    def to_bytes_der(self) -> bytes:
        """DER-encoded public key."""
        return self._public_key.public_bytes(
            encoding=serialization.Encoding.DER,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    def to_string(self) -> str:
        """
        Returns the private key as a hex string (raw).
        Matches old usage that calls to_string().
        """
        return self.to_string_raw()

    def to_string_der(self) -> str:
        """Hex-encoded DER form of the public key."""
        return self.to_bytes_der().hex()

    def to_string_raw(self) -> str:
        """
        Kept for old usage: returns the raw hex-encoded public key.
        For new usage, prefer `to_string_raw()` or `to_string_der()`.
        """
        """
        Returns the raw public key as a hex-encoded string.
        """
        return self.to_bytes_raw().hex()

    def to_proto(self):
        """
        Returns the protobuf representation of the public key.
        For Ed25519, uses the 'ed25519' field.
        For ECDSA, uses 'ECDSASecp256k1'.

        Returns:
            Key: The protobuf Key message.
        """
        from hiero_sdk_python.hapi.services import basic_types_pb2

        pub_bytes = self.to_bytes_raw()
        if self.is_ed25519():
            return basic_types_pb2.Key(ed25519=pub_bytes)
        else:
            return basic_types_pb2.Key(ECDSA_secp256k1=pub_bytes)

    def is_ed25519(self) -> bool:
        """
        Checks if this public key is Ed25519.
        """
        return isinstance(self._public_key, ed25519.Ed25519PublicKey)

    def is_ecdsa(self) -> bool:
        """
        Checks if this public key is ECDSA (secp256k1).
        """
        return isinstance(self._public_key, ec.EllipticCurvePublicKey)

    def __repr__(self):
        if self.is_ed25519():
            return f"<PublicKey (Ed25519) hex={self.to_string_raw()}>"
        return f"<PublicKey (ECDSA) hex={self.to_string_raw()}>"