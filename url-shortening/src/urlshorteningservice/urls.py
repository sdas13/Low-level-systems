from flask import Blueprint
from flask_restful import Api, Resource
from apps.create import CreateUrl

api_bp = Blueprint("api", __name__)
api = Api(api_bp)

api.add_resource(CreateUrl, "/createURL")
