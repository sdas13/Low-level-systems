from flask_mongoengine import MongoEngine
from flask_redis import FlaskRedis

db = MongoEngine()
redis_client = FlaskRedis()