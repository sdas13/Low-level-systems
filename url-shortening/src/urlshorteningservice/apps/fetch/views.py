from flask import request, redirect
from flask_restful import Resource
from apps.models import URL


class FetchUrl(Resource):
    def get(self, key):
        hashedParam = key
        document = URL.objects(hashedParam=hashedParam).first()
        return redirect(document.originalURL)
