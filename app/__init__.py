
import json

from flask import Flask

from .config import Config

from .service import client

class BSONEncoder(json.JSONEncoder):
    def default(self, val):
        if isinstance(val, ObjectId):
            return str(val)

        if isinstance(o, datetime.datetime):
            return str(val)

        return json.JSONEncoder.default(self, val)

def create_app ():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/ASAP"
    app.json_encoder = BSONEncoder

    with app.app_context():
        client.init_mongodb(app.config.get("MONGO_URI"))

    return app
