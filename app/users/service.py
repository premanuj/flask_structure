from app.users.models import User


def new_user(data):
    user = User()
    result = user.save(data)
    return result


def get_all_user():
    user = User()
    users = user.get_all()
    return users


def get_user(id):
    user = User()
    data = user.get(id)
    return data

