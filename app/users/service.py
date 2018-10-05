from datetime import datetime, timedelta

import jwt
from app.utils.custom_exception import DataNotFound
from flask import abort

from app.users.models import User


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
    return users


def get_user(id):
    user = User()
    data = user.get(id)
    if data is None:
        raise DataNotFound("No user exist")

    return data


def login(auth):
    user = User()
    data = user.login(auth)
    if not data:
        abort(401)
    if data.check_password(auth.password):
        token = jwt.encode({"id": user.id, "exp": datetime.utcnow() + timedelta(minutes=30)})
        return token
    abort(401)

