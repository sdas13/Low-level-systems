from clients import redis


def load_keys_into_cache():
    return redis.get("potato")
