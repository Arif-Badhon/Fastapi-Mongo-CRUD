from fastapi import APIRouter
from models.user import User, Admin
from database.database import user_collection
from schemas.user import serializeDict, serializeList
from bson import ObjectId

user =APIRouter()

#for admin
@user.get('/all_admin')
def find_all_admin():
    return serializeList(user_collection.find({'role' : 'admin'}))

@user.post('/add_admin')
def create_admin(admin: Admin):
    admin.role = 'admin'
    admin.type= None
    user_collection.insert_one(dict(admin))
    return serializeList(user_collection.find({'role' : 'admin'}))

@user.patch('/edit_admin_data/{id}')
def edit_admin(id, admin: Admin):
    user_collection.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(admin)})
    return serializeDict(user_collection.find_one({"_id":ObjectId(id)}))

@user.delete('/delete_admin/{id}')
def delete_admin(id, admin: Admin):
    return serializeDict(user_collection.find_one_and_delete({"_id": ObjectId(id)}))

#for user
@user.get('/all_user')
def find_all_user():
    return serializeList(user_collection.find())

@user.put('/edit_user_data/{id}')
def edit_user_data(id, user: User):
    user_collection.find_one_and_update({"_id": ObjectId(id)},{"$set":dict(user)})
    return serializeDict (user_collection.find_one({"_id":ObjectId(id)}))

@user.delete('/delete_user/{id}')
def delete_user(id, user: User):
    return serializeDict(user_collection.find_one_and_delete({"_id": ObjectId(id)}))

#For Indivisual User
@user.post('/create_individual_basic_user')
def create_user(user : User):
    user.role = 'individual_user'
    user.type = 'basic'
    user_collection.insert_one(dict(user))
    return serializeList(user_collection.find())

@user.post('/create_individual_standard_user')
def create_user(user : User):
    user.role = 'individual_user'
    user.type = 'standard'
    user_collection.insert_one(dict(user))
    return serializeList(user_collection.find())

@user.post('/create_individual_professional_user')
def create_user(user : User):
    user.role = 'individual_user'
    user.type = 'professional'
    user_collection.insert_one(dict(user))
    return serializeList(user_collection.find())

#for coorporate user
@user.post('/create_corporate_basic_user')
def create_user(user : User):
    user.role = 'corporate_user'
    user.type = 'basic'
    user_collection.insert_one(dict(user))
    return serializeList(user_collection.find())

@user.post('/create_corporate_standard_user')
def create_user(user : User):
    user.role = 'corporate_user'
    user.type = 'standard'
    user_collection.insert_one(dict(user))
    return serializeList(user_collection.find())

@user.post('/create_corporate_professional_user')
def create_user(user : User):
    user.role = 'corporate_user'
    user.type = 'professional'
    user_collection.insert_one(dict(user))
    return serializeList(user_collection.find())
