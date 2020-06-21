from pymongo import MongoClient
from config import server


def init():
    return MongoClient(server.MONGO_URI).get_database('flask_api')
