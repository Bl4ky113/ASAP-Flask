
import time

from flask import g

from app import create_app

app = create_app()

@app.before_request
def before_request ():
    g.start_time = time.time()

@app.after_request
def after_request (response):
    g.end_time = time.time()
    diff = g.end_time - g.start_time

    app.logger.info(f"TIME START; END; DIFFERENCE: {g.start_time}; {g.end_time}; {diff}")

    return response

@app.route("/ping", methods=("GET", ))
def ping ():
    return "Pong"
