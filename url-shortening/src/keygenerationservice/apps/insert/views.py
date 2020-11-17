from flask import Blueprint
from apps.insert.models import OfflineKeys
import random, string

bp = Blueprint("api", __name__)


@bp.route("/insert", methods=["GET"])
def insert():

    key_list = []
    for i in range(1000):
        str = "".join(random.choices(string.ascii_letters + string.digits, k=6))
        key_list.append(OfflineKeys(key=str))

    OfflineKeys.objects.insert(key_list)

    return "hello"
