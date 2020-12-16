from clients import redis_client
from apps.insert import OfflineKeys
import time


def load_keys_into_cache():
    collection = OfflineKeys._get_collection()

    start_time = time.time()
    data = collection.find({}, {"_id": 0}).limit(500000)
    offline_keys = list(map(lambda i: i["key"], data))

    collection.delete_many({"key": {"$in": offline_keys}})
    redis_client.lpush("offline_keys", *offline_keys)

    print(round(time.time() - start_time, 2))
    return str(redis_client.llen("offline_keys"))
