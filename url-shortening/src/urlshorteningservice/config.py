class Config:
    SECRET = "my_precious"


class DevConfig(Config):
    ENV = "development"
    DEBUG = True
    TESTING = True
    MONGODB_SETTINGS = {"db": "urlShorteningDB"}


class ProdConfig(Config):
    DEBUG = False
    TESTING = False
