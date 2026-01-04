from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta

client = MongoClient(settings.MONGO_URI)
db = client[settings.MONGO_DB]
pads_collection = db["pads"]


def ensure_ttl_index():
    pads_collection.create_index(
        "last_accessed_at",
        expireAfterSeconds=int(timedelta(days=60).total_seconds())
    )
