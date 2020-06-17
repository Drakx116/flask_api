from flask import jsonify
from bin import app
from bin.functions.api import json_response

app = app.init()


@app.route('/', methods={ 'GET' })
def alive():
    return jsonify({ 'message': 'Welcome on a Flask API.' }), 200


@app.route('/auth/login', methods={ 'POST' })
def login():
    return json_response(501)


if __name__ == '__main__':
    app.run()
