
from bson.objectid import ObjectId
from bson.errors import InvalidId

from . import client

STUDENT_COLLECTION = "students"

db = client.connect_to_db()

def get_students ():
    try:
        students_list = [doc for doc in db.students.find({})]
        students_num = len(students_list)

        return students_list, students_num

    except Exception as error:
        return error, -2

def get_student_by_id (student_id):
    try:
        try:
            student_info = db.students.find_one({"_id": ObjectId(student_id)})
            student_count = 1 if student_info else 0
        except InvalidId as error:
            return error, -1

        return student_info, student_count

    except Exception as error:
        return error, -2

def delete_student_by_id (student_id):
    try:
        try:
            student_info = db.students.delete_one({"_id": ObjectId(student_id)})
            student_count = 1 if student_info else 0
        except InvalidId as error:
            return error, -1

        return student_info, student_count

    except Exception as error:
        return error, -2

