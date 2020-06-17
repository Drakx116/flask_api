from flask import jsonify
from bin import app

app = app.init()


@app.route('/', methods={ 'GET' })
def alive():
    return jsonify({ 'message': 'Welcome on a Flask API.' }), 200


@app.route('/auth/login', methods={ 'POST' })
def login():
    return jsonify({ 'message': 'Route not implemented yet.' }), 404


if __name__ == '__main__':
    app.run()
