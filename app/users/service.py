from app.users.models import User
from app.utils.custom_exception import DataNotFound


def new_user(data):
    user = User()
    result = user.save(data)
    result = {
        "id": result.id,
        "username": result.username,
        "user_type": str(result.user_type),
        "email": result.email_address,
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

