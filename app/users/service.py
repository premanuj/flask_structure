from app.users.models import User


def new_user(data):
    user = User()
    result = user.save(data)
    print(result)
    return result


def get_all_user():
    user = User()
    users = user.get_all()
    print(users)
    return users

