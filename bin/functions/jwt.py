from flask_jwt_extended import JWTManager, create_access_token


def generate_token(username):
    return create_access_token(username)


