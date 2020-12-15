from clients import db


class OfflineKeys(db.Document):
    key = db.StringField(required=True, unique=True)

    meta = {"indexes": ["key"]}
