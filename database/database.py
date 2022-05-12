from decouple import config
from .database_helper import role_helper, user_helper
from bson import ObjectId
from pymongo import MongoClient


MONGO_DETAILS = config('MONGO_DETAILS')
port = 8000
client = MongoClient(MONGO_DETAILS, port)
db = client["practiceauth"]

user_collection = db.get_collection('user')
role_collection = db.get_collection('role')

#for User

def retrieve_user(id: str)-> dict:
    user = user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(user)

def add_user(user_data: str)-> dict:
    user = user_collection.insert_one(user_data)
    new_user = user_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)

def update_user(id: str, data: dict):
    user = user_collection.find_one({"_id": ObjectId(id)})
    if user:
        user_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    return True

def delete_user(id: str):
    user = user_collection.find_one({"_id": ObjectId(id)})
    if user:
        user_collection.delete_one({"_id": ObjectId(id)})
        return True

#roles

def retrieve_role(id: str)-> dict:
    role = role_collection.find_one({"_id": ObjectId(id)})
    if role:
        return role_helper(role)

def add_role(role_data: str) -> dict:
    role = role_collection.insert_one(role_data)
    new_role = role_collection.find_one({"_id": role.inserted_id})
    return role_helper(role)

def update_role(id: str, data: dict):
    role = role_collection.find_one({"_id": ObjectId(id)})
    if role:
        role_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return True

def delete_role(id: str):
    role = role_collection.find_one({"_id": ObjectId(id)})
    if role:
        role_collection.delete_one({"_id": ObjectId(id)})
        return True
