import base64
import codecs

def decode_base64(encoded_str):
    """Decode Base64 encoded string."""
    try:
        return base64.b64decode(encoded_str).decode("utf-8")
    except Exception:
        return None

def decode_hex(encoded_str):
    """Decode Hex encoded string."""
    try:
        return bytes.fromhex(encoded_str).decode("utf-8")
    except Exception:
        return None

def decode_rot13(encoded_str):
    """Decode ROT13 encoded string."""
    try:
        return codecs.decode(encoded_str, "rot_13")
    except Exception:
        return None
