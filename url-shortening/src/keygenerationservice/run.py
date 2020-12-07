from flask import Flask
from urls import bp
from clients import db, redis_client


def init_app():

    app = Flask(__name__)
    app.config.from_object("config.DevConfig")
    app.register_blueprint(bp, url_prefix="/kgs")
    db.init_app(app)
    redis_client.init_app(app)
    return app


if __name__ == "__main__":
    app = init_app()
    app.run(port=5001)
