from flask import request
from flask_restful import Resource
from apps.create import OfflineKeys
from apps.models import URL


class CreateUrl(Resource):
    def post(self):
        url = request.json["url"]
        print(url)
        document = OfflineKeys.objects.first()
        document.delete()
        hashedParam = document.key
        URL(hashedParam=hashedParam, originalURL=url).save()
        return "localhost:5000/" + hashedParam
