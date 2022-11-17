import logging
import os
from flask import Flask
from flask_cors import CORS
from flask_bcrypt import Bcrypt


cors = CORS()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)

    app_settings = os.environ.get(
        "APP_SETTINGS", "project.config.BaseConfig")
    app.config.from_object(app_settings)
    app.logger.setLevel(logging.INFO)
    cors.init_app(app)
    bcrypt.init_app(app)

    from project.apis import api
    api.init_app(app)

    return app
