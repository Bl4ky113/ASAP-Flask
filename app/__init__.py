
from flask import Flask
from flask_pymongo import PyMongo

from .config import Config

def create_app ():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo = PyMongo(app)

    return app
