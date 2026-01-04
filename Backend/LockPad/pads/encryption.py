import os
from cryptography.fernet import Fernet

# Encryption key should come from ENV
FERNET_KEY = os.getenv("LOCKPAD_FERNET_KEY")

if not FERNET_KEY:
    raise RuntimeError("LOCKPAD_FERNET_KEY not set")

fernet = Fernet(FERNET_KEY.encode())


def encrypt_text(plain_text: str) -> str:
    return fernet.encrypt(plain_text.encode()).decode()


def decrypt_text(cipher_text: str) -> str:
    return fernet.decrypt(cipher_text.encode()).decode()
