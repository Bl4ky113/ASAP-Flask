
from flask import Response, request, current_app

from bson import json_util

from mongoengine.errors import FieldDoesNotExist, ValidationError

from . import student

from ..service.student_service import *
from ..models.student_model import StudentModel

@student.route("/", methods=("GET", ), defaults={"student_id": None})
@student.route("/<student_id>", methods=("GET", ))
def get_students_route (student_id):
    try:
        return_student_list = None
        count_student_list = 0

        if student_id is not None:
            return get_student_by_id_route(student_id)

        return_student_list, count_student_list = get_students()

        if count_student_list == -2:
            return Response(
                json_util.dumps({
                    "error": "GENERAL students MODULE ERROR",
                    "data": str(return_student_list),
                    "code": 100-0
                })
            )

        return Response(
            json_util.dumps({
                "data": return_student_list,
                "count": count_student_list
            }),
            200,
            mimetype="application/json"
        )

    except Exception as error:
        return Response(
            json_util.dump({
                "error": "GENERAL students MODULE ERROR",
                "data": str(error),
                "code": 100-1
            },
            500,
            mimetype="application/json"
        )
        )


def get_student_by_id_route (student_id):
    try:
        return_student = None
        count_student = 0

        return_student, count_student = get_student_by_id(student_id)

        if count_student == -2:
            return Response(
                json_util.dumps({
                    "error": "GENERAL student MODULE ERROR",
                    "data": str(return_student),
                    "code": 100-2
                }),
                500,
                mimetype="application/json"
            )

        if count_student == -1:
            return Response(
                json_util.dumps({
                    "error": f"ObjectId {student_id} NOT VALID",
                    "data": str(return_student),
                    "code": 101
                }),
                404,
                mimetype="application/json"
            )

        if return_student is None and count_student != 1:
            return Response(
                json_util.dumps({
                    "error": f"student with id {student_id} NOT FOUND",
                    "code": 102
                }),
                404,
                mimetype="application/json"
            )

        return Response(
            json_util.dumps({
                "data": return_student,
                "count": count_student
            }),
            200,
            mimetype="application/json"
        )

    except Exception as error:
        return Response(
            json_util.dumps({
                "error": "GENERAL student MODULE ERROR",
                "data": str(error),
                "code": 100-3
            }),
            500,
            mimetype="application/json"
        )

@student.route("/", methods=("POST", "PUT"), defaults={"student_id": None})
@student.route("/<string:student_id>", methods=("POST", "PUT"))
def post_student_route (student_id):
    try:
        if not request.is_json:
            return Response(
                json_util.dumps({
                    "error": "REQUEST IS NOT application/json TYPE",
                    "data": f"request.is_json -> {request.is_json}",
                    "code": 103
                }),
                403,
                mimetype="application/json"
            )

        request_data = request.get_json()
        student_fields = StudentModel._fields.keys()
        student_data = {}
        student_doc = None
        student_saved = None

        for field in student_fields:
            try:
                if field == "id":
                    continue

                student_data[field] = request_data[field]
            except KeyError as warning:
                current_app.logger.warning(f"STUDENT DATA FIELD ({field}) NOT PASSED")
        
        try:
            student_doc = StudentModel(**student_data)

        except FieldDoesNotExist as error:
            return Response(
                json_util.dumps({
                    "error": "student_data HAS FIELDS NOT DEFINED IN StudentModel",
                    "data": error.args,
                    "code": 104
                }),
                400,
                mimetype="application/json"
            )


        try:
            student_saved = student_doc.save()

        except ValidationError as error:
            return Response(
                json_util.dumps({
                    "error": "StudentModel FIELDS VALIDATION FAILED",
                    "data": error.to_dict(),
                    "code": 105
                }),
                400,
                mimetype="application/json"
            )

        student_data["id"] = student_saved.id

        return Response(
            json_util.dumps({
                "data": student_data,
                "count": 1
            }),
            200,
            mimetype="application/json"
        )
    
    except Exception as error:
        return Response(
            json_util.dumps({
                "error": "GENERAL student MODULE ERROR",
                "data": str(error),
                "code": 100-4
            }),
            500,
            mimetype="application/json"
        )

def update_student (request_data, student_id):
    return f"{student_id}"

@student.route("/<int:student_id>", methods=("DELETE", ))
def delete_student (student_id):
    return f"{student_id}"
