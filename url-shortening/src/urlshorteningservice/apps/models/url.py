from clients import db
import datetime


class URL(db.Document):
    originalURL = db.StringField(max_length=512, required=True)
    hashedParam = db.StringField(max_length=8, required=True, unique=True)
    creationDate = db.DateTimeField(default=datetime.datetime.utcnow)
    expirationDate = db.DateTimeField()

    meta = {"collection": "URL"}