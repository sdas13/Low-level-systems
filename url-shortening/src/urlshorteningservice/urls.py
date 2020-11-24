from flask import Blueprint
from flask_restful import Api, Resource
from apps import CreateUrl, FetchUrl

api_bp = Blueprint("api", __name__)
api = Api(api_bp)

api.add_resource(CreateUrl, "/api/createURL")
api.add_resource(FetchUrl, "/<string:key>")