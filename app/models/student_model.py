
from mongoengine import *

class StudentModel (Document):
    name = StringField(required=True)
    lastname = StringField(required=True)
    age = DecimalField(min_value=0, required=True)
    major = StringField(required=True)
    password = StringField()

    meta = {'collection': 'students'}
