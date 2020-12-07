import random, string
from apps.insert import OfflineKeys


def insert_keys():

    print("Request: Offline keys to be inserted...")
    i = 0
    while i < 500000:
        try:
            rand_key = "".join(
                random.choices(string.ascii_letters + string.digits, k=6)
            )
            # key_list.append(OfflineKeys(key=rand_key))
            OfflineKeys(key=rand_key).save()
            i += 1
        except Exception as e:
            print("Exception ", e)
            continue

    print("Done...")

    # OfflineKeys.objects.insert(key_list)
    # return OfflineKeys.objects.exclude("id").limit(100).to_json()
    return str(OfflineKeys.objects.count())
