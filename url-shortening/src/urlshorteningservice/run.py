from flask import Flask
from urls import api_bp


def init_app():

    app = Flask(__name__)
    app.config.from_object("config.DevConfig")
    app.register_blueprint(api_bp, url_prefix="/api")

    return app


if __name__ == "__main__":
    app = init_app()
    app.run()
