from datetime import datetime, timedelta

import jwt
from app.utils.custom_exception import DataNotFound
from flask import abort

from app.users.models import User, Contact
from app.users.schema import user_schema, users_schema, profile_schema, profiles_schema


def new_user(data):
    user = User()
    result = user.save(data)
    result = {
        "id": result.id,
        "username": result.username,
        "user_type": str(result.user_type),
        "email": result.email_address,
        "password": result.password_hash,
    }
    return result


def get_all_user():
    user = User()
    users = user.get_all()
    result = users_schema.dump(users)
    data = []
    for user in result:
        contacts = user["contacts"][0]
        value = {key: val for key, val in user.items() if key != "contacts"}
        data.append({**value, **contacts})
    return data


def get_user(id):
    user = User()
    data = user.get(id)
    if data is None:
        raise DataNotFound("No user exist")
    result = user_schema.dump(data)
    contacts = result["contacts"][0]
    value = {key: val for key, val in result.items() if key != "contacts"}
    return {**value, **contacts}


def login(auth):
    user = User()
    data = user.login(auth)
    if not data:
        abort(401)
    if data.check_password(auth.password):
        token = jwt.encode({"id": user.id, "exp": datetime.utcnow() + timedelta(minutes=30)})
        return token
    abort(401)


def user_profile(data):
    user = Contact()
    result = user.save(data)
    if not result:
        raise DataNotFound("No contact availble for this user")
    result = {
        "id": result.id,
        "first_name": result.first_name,
        "last_name": result.last_name,
        "user_id": result.user_id,
    }
    return result


def get_all_profile():
    user = Contact()
    result = user.get_all()
    return result
