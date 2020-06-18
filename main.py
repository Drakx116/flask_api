from flask import jsonify, request
from flask_jwt_extended import JWTManager, jwt_required
from bin import app
from bin.functions.api import json_response
from bin.functions.jwt import generate_token

app = app.init()
jwt = JWTManager(app)


@app.route('/', methods={ 'GET' })
@jwt_required
def alive():
    return jsonify({ 'message': 'Welcome on a Flask API.' }), 200


@app.route('/auth/login', methods={ 'POST' })
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    if not username and password:
        return json_response(422)

    token = generate_token(username)
    response = { 'token': token }
    return json_response(200, response)


if __name__ == '__main__':
    app.run()
