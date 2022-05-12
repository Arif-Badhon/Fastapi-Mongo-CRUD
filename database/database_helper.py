def user_helper(user) -> dict:
    return {
        "id": str(user['_id']),
        "fullname": user['fullname'],
        "email": user['email'],
        "designation": user['designation'],
        "company": user['company'],
        "password": user['password'],
        "role": user['role'],
        "type": user['type']
    }

def role_helper(user) -> dict:
    return {
        "id": str(user['_id']),
        "role_id": user['role_id'],
        "type": user['type']
    }