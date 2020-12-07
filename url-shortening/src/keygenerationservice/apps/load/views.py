from clients import redis_client
from apps.insert import OfflineKeys


def load_keys_into_cache():
    collection = OfflineKeys._get_collection()

    data = collection.find({}, {"_id": 0}).limit(10000)
    offline_keys = list(map(lambda i: i["key"], data))

    collection.delete_many({"key": {"$in": offline_keys}})
    redis_client.lpush("offline_keys", *offline_keys)

    return str(redis_client.llen("offline_keys"))
