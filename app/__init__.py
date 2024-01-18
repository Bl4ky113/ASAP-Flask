
from flask import Flask

from .config import Config

from .service import client

from .student import student

def create_app ():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/ASAP"

    with app.app_context():
        client.init_mongodb(app.config.get("MONGO_URI"))

    app.register_blueprint(student)

    return app
