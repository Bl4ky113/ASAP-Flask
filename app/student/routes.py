
from flask import Response, Request

from bson import json_util

from . import student

from ..service.student_service import *

@student.route("/", methods=("GET", ), defaults={"student_id": None})
@student.route("/<student_id>", methods=("GET", ))
def get_students_route (student_id):
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
                    "code": 100-1
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
                "code": 100-2
            }),
            500,
            mimetype="application/json"
        )

@student.route("/<int:student_id>", methods=("POST", ))
def index ():
    return Response(
        json_util.dumps("HELLO"),
        200,
        mimetype="application/json"
    )

@student.route("/<int:student_id>", methods=("PUT", "PATCH"))
def update_student (student_id):
    return f"{student_id}"

@student.route("/<int:student_id>", methods=("DELETE", ))
def delete_student (student_id):
    return f"{student_id}"
