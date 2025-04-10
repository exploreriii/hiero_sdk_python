import warnings
from cryptography.hazmat.primitives.asymmetric import ed25519, ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from typing import Optional, Union
from hiero_sdk_python.crypto.public_key import PublicKey
from cryptography.hazmat.primitives import hashes

class PrivateKey:
    """
    Represents a private key that can be either Ed25519 or ECDSA (secp256k1).
    """

    def __init__(
        self, private_key: Union[ec.EllipticCurvePrivateKey, ed25519.Ed25519PrivateKey]):
        """
        Initializes a PrivateKey from a cryptography PrivateKey object.
        """
        self._private_key = private_key

    #
    # -----------------------
    # Type-specific generators
    # -----------------------
    #

    @classmethod
    def generate(cls, key_type: str = "ed25519"):
        if key_type.lower() == "ed25519":
            return cls.generate_ed25519()
        elif key_type.lower() == "ecdsa":
            return cls.generate_ecdsa()
        else:
            raise ValueError("Invalid key_type. Use 'ed25519' or 'ecdsa'.")
 
    @classmethod
    def generate_ed25519(cls) -> "PrivateKey":
        return cls(ed25519.Ed25519PrivateKey.generate())

    @classmethod
    def generate_ecdsa(cls) -> "PrivateKey":
        private_key = ec.generate_private_key(ec.SECP256K1(), default_backend())
        return cls(private_key)

    #
    # -----------------------------------
    # Type-specific 'from string' loaders
    # -----------------------------------
    #

    @classmethod
    def from_string_ed25519(cls, hex_str: str) -> "PrivateKey":
        """
        Interpret the given string as a hex-encoded 32-byte seed for Ed25519.
        """
        hex_str = hex_str.removeprefix("0x")
        try:
            seed = bytes.fromhex(hex_str)
        except ValueError:
            raise ValueError(f"Invalid hex string for Ed25519 seed: {hex_str}")
        return cls.from_bytes_ed25519(seed)

    @classmethod
    def from_string_ecdsa(cls, hex_str: str) -> "PrivateKey":
        """
        Interpret the given string as a hex-encoded 32-byte scalar for ECDSA secp256k1.
        """
        hex_str = hex_str.removeprefix("0x")
        try:
            scalar = bytes.fromhex(hex_str)
        except ValueError:
            raise ValueError(f"Invalid hex string for ECDSA scalar: {hex_str}")
        return cls.from_bytes_ecdsa(scalar)

    @classmethod
    def from_string_der(cls, hex_str: str) -> "PrivateKey":
        """
        Interpret the given string as hex-encoded DER bytes containing a private key.
        """
        hex_str = hex_str.removeprefix("0x")
        try:
            der_bytes = bytes.fromhex(hex_str)
        except ValueError:
            raise ValueError(f"Invalid hex string for DER private key: {hex_str}")
        return cls.from_der(der_bytes)

    #
    # ---------------------------------
    # Type-specific 'from bytes' loaders
    # ---------------------------------
    #

    @classmethod
    def from_bytes_ed25519(cls, seed: bytes) -> "PrivateKey":
        """
        Load an Ed25519 private key from a 32-byte raw seed.
        Raises ValueError if not exactly 32 bytes or invalid for Ed25519.
        """
        if len(seed) != 32:
            raise ValueError(f"Ed25519 seed must be exactly 32 bytes, got {len(seed)}.")
        try:
            ed_priv = ed25519.Ed25519PrivateKey.from_private_bytes(seed)
            return cls(ed_priv)
        except Exception as e:
            raise ValueError(f"Invalid Ed25519 private seed: {e}")

    @classmethod
    def from_bytes_ecdsa(cls, scalar: bytes) -> "PrivateKey":
        """
        Load an ECDSA secp256k1 private key from a 32-byte scalar.
        Raises ValueError if not 32 bytes or invalid scalar.
        """
        if len(scalar) != 32:
            raise ValueError(f"ECDSA (secp256k1) scalar must be 32 bytes, got {len(scalar)}.")
        try:
            private_int = int.from_bytes(scalar, "big")
            ec_priv = ec.derive_private_key(private_int, ec.SECP256K1(), default_backend())
            return cls(ec_priv)
        except Exception as e:
            raise ValueError(f"Invalid ECDSA secp256k1 scalar: {e}")

    @classmethod
    def from_der(cls, der_bytes: bytes) -> "PrivateKey":
        """
        Load a private key from DER-encoded bytes (PKCS#8, TraditionalOpenSSL, etc.).
        Detects Ed25519 vs ECDSA (secp256k1). Raises ValueError if unsupported or invalid.
        """
        try:
            private_key = serialization.load_der_private_key(der_bytes, password=None)
        except Exception as e:
            raise ValueError(f"Could not parse DER private key: {e}")

        # Check Ed25519
        if isinstance(private_key, ed25519.Ed25519PrivateKey):
            return cls(private_key)

        # Check ECDSA
        if isinstance(private_key, ec.EllipticCurvePrivateKey):
            if not isinstance(private_key.curve, ec.SECP256K1):
                raise ValueError("Only secp256k1 ECDSA keys are supported.")
            return cls(private_key)

        raise ValueError("Unsupported private key type in DER (not Ed25519 or ECDSA).")


    #
    # ------------------------
    # Other
    # ------------------------
    #

    def sign(self, data: bytes) -> bytes:
        """Sign the given data using this private key."""
        if self.is_ed25519():
            return self._private_key.sign(data)
        else:
            # ECDSA requires specifying a hash algorithm
            from cryptography.hazmat.primitives.asymmetric import ec
            return self._private_key.sign(data, ec.ECDSA(hashes.SHA256()))
        
    def public_key(self) -> PublicKey:
        """Derive the corresponding PublicKey."""
        return PublicKey(self._private_key.public_key())

    def to_bytes_raw(self) -> bytes:
        """
        Return the raw bytes of the private key:
          - Ed25519: 32-byte seed
          - ECDSA: 32-byte scalar
        """
        if self.is_ed25519():
            return self._private_key.private_bytes(
                encoding=serialization.Encoding.Raw,
                format=serialization.PrivateFormat.Raw,
                encryption_algorithm=serialization.NoEncryption()
            )
        else:
            # ECDSA
            return self._private_key.private_numbers().private_value.to_bytes(32, "big")

    def to_bytes_der(self) -> bytes:
        """
        Return the private key in DER format (PKCS#8 / TraditionalOpenSSL).
        """
        return self._private_key.private_bytes(
            encoding=serialization.Encoding.DER,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
    
    def to_string_raw(self) -> str:
        """Hex-encoded form of `to_bytes_raw()`."""
        return self.to_bytes_raw().hex()

    def to_string_der(self) -> str:
        """Hex-encoded DER form of the private key."""
        return self.to_bytes_der().hex()

    def is_ed25519(self) -> bool:
        """Return True if this is an Ed25519 private key."""
        return isinstance(self._private_key, ed25519.Ed25519PrivateKey)

    def is_ecdsa(self) -> bool:
        """Return True if this is an ECDSA (secp256k1) private key."""
        return isinstance(self._private_key, ec.EllipticCurvePrivateKey)

    def __repr__(self):
        if self.is_ed25519():
            return f"<PrivateKey (Ed25519) hex={self.to_string_raw()}>"
        return f"<PrivateKey (ECDSA) hex={self.to_string_raw()}>"
    
    def to_string(self) -> str:
        """
        Returns the private key as a hex string (raw) (32 bytes).
        Matches old usage that calls to_string(). 
        For new usage, prefer `to_string_raw()` or `to_string_der().
        """
        return self.to_string_raw()