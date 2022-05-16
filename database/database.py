from decouple import config
from bson import ObjectId
from pymongo import MongoClient


MONGO_DETAILS = config('MONGO_DETAILS')
port = 8000
client = MongoClient(MONGO_DETAILS, port)
db = client["practiceauth"]

user_collection = db.get_collection('user')
