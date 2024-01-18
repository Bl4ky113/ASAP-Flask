
from pymongo import MongoClient

from mongoengine import connect

class Database ():
    db = None
    mongo = None
    path = None

    def __init__ (self):
        return

    def init_mongodb (self, mongo_path):
        self.path = mongo_path
        self.db = self.connect_to_db()
        self.connect_odm_to_db()
        return

    def connect_to_db (self):
        self.mongo = MongoClient(self.path)
        self.db = self.mongo["ASAP"]
        return self.db

    def connect_odm_to_db (self):
        connect(host=self.path)

client = Database()
