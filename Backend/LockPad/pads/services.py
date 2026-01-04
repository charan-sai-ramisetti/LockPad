import hashlib
from datetime import datetime, timezone
from django.conf import settings
from pymongo import MongoClient

from .encryption import encrypt_text, decrypt_text

client = MongoClient(settings.MONGO_URI)
db = client[settings.MONGO_DB]
pads_collection = db["pads"]


def _hash_key(raw_key: str) -> str:
    return hashlib.sha256(raw_key.encode()).hexdigest()


def open_or_create_pad(raw_key: str) -> str:
    key_hash = _hash_key(raw_key)
    now = datetime.now(timezone.utc)

    pad = pads_collection.find_one({"key_hash": key_hash})

    if pad:
        pads_collection.update_one(
            {"key_hash": key_hash},
            {"$set": {"last_accessed_at": now}}
        )
        return decrypt_text(pad["encrypted_content"])

    # Create new pad
    pads_collection.insert_one({
        "key_hash": key_hash,
        "encrypted_content": encrypt_text(""),
        "created_at": now,
        "last_accessed_at": now
    })

    return ""


def save_pad(raw_key: str, content: str) -> None:
    key_hash = _hash_key(raw_key)
    now = datetime.now(timezone.utc)

    encrypted = encrypt_text(content)

    pads_collection.update_one(
        {"key_hash": key_hash},
        {
            "$set": {
                "encrypted_content": encrypted,
                "last_accessed_at": now
            }
        },
        upsert=True
    )
