from .. import db
from ..models.user import UserModel
  
def find_by_username(username):
    return UserModel.query.filter_by(username=username).first()

def find_by_id(id):
    return UserModel.query.filter_by(id=id).first()

def save(user):
    db.session.add(user)
    db.session.commit()