import random, string
from apps.insert import OfflineKeys


def insert_keys():

    key_list = []
    for i in range(50000):
        rand_key = "".join(random.choices(string.ascii_letters + string.digits, k=6))
        key_list.append(OfflineKeys(key=rand_key))

    OfflineKeys.objects.insert(key_list)
    # return OfflineKeys.objects.exclude("id").limit(10000).to_json()
    return str(OfflineKeys.objects.count())
