from flask import jsonify, request
from bin import app
from bin.functions.api import json_response

app = app.init()


@app.route('/', methods={ 'GET' })
def alive():
    return jsonify({ 'message': 'Welcome on a Flask API.' }), 200


@app.route('/auth/login', methods={ 'POST' })
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    if not username and password:
        return json_response(422)

    # Todo : Create a token dedicated service
    token = None
    response = { 'token': token }
    return json_response(200, response)


if __name__ == '__main__':
    app.run()
