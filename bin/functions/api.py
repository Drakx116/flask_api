from flask import jsonify


def json_response(status, data = None):
    if data:
        return jsonify(data), status

    if status == 200:
        return jsonify({ 'data': 'Success.' }), 200
    elif status == 201:
        message = 'Resource created.'
    elif status == 204:
        message = 'Resource deleted.'
    elif status == 400:
        message = 'Bad request.'
    elif status == 401:
        message = 'Unauthorized.'
    elif status == 405:
        message = 'Method not allowed.'
    elif status == 422:
        message = 'Invalid request parameters.'
    elif status == 498:
        message = 'Invalid token.'
    elif status == 501:
        message = 'Route not implemented.'
    else:
        status = 500
        message = 'Internal server error.'

    return jsonify({ 'error': message }), status
