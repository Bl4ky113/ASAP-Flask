
from . import client

STUDENT_COLLECTION = "students"

db = client.connect_to_db()

def get_students ():
    return db.students.find_one()
