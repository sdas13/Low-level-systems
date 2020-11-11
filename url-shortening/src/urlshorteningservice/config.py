class Config:
    SECRET = "my_precious"


class DevConfig(Config):
    ENV = "development"
    DEBUG = True
    TESTING = True


class ProdConfig(Config):
    DEBUG = False
    TESTING = False
