
from flask import jsonify
from flask import Response

from bson import json_util

from app import create_app
from app.service.student_service import get_students

app = create_app()
db = get_students()

@app.route('/')
def index ():
    return Response(
        json_util.dumps(get_students()),
        200,
        mimetype="application/json"
    )
