from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80))
    _password_hash = db.Column('password_hash', db.String(256))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def password(self):
        return self._password_hash

    @password.setter
    def password(self, password):
        self._password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)
