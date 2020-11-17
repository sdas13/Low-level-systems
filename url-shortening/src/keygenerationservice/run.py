from flask import Flask
from apps.insert.views import bp
from init_db import db


def init_app():

    app = Flask(__name__)
    app.config.from_object("config.DevConfig")
    app.register_blueprint(bp, url_prefix="/kgs")
    db.init_app(app)
    return app


if __name__ == "__main__":
    app = init_app()
    app.run()
