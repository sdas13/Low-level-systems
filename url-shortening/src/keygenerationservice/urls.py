from flask import Blueprint
from apps import insert_keys, load_keys_into_cache

bp = Blueprint("api", __name__)


@bp.route("/insert", methods=["GET"])
def insert():
    return insert_keys()


@bp.route("/load", methods=["GET"])
def load():
    return load_keys_into_cache()
