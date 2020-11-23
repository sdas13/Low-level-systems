class Config:
    SECRET = "my_precious"


class DevConfig(Config):
    ENV = "development"
    DEBUG = True
    TESTING = True
    MONGODB_SETTINGS = {"db": "urlShorteningDB"}
    REDIS_URL = "redis://localhost:6379/0"


class ProdConfig(Config):
    DEBUG = False
    TESTING = False
