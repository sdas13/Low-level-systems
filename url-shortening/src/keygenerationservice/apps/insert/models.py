from init_db import db


class OfflineKeys(db.Document):
    key = db.StringField(required=True, unique=True)
