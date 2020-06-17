from flask import jsonify
from bin import app

app = app.init()


@app.route('/', methods={ 'GET' })
def alive():
    return jsonify({ 'message': 'Welcome on a Flask API.' })


if __name__ == '__main__':
    app.run()
