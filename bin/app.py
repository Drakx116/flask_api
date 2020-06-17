from flask import Flask


def init():
    app = Flask(__name__)
    app.config.from_pyfile('../config/server.py')
    return app
