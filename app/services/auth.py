from ..repositories.user import find_by_username, find_by_id

def authenticate(username, password):
    user = find_by_username(username)

    if user and user.verify_password(password):
        return user

def identity(payload):
    return find_by_id(payload['identity'])
