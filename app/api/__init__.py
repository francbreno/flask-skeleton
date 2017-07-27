from flask import Blueprint
from flask_restful import Api
from .user import UserRegister

def create_api_bp():
  bp = Blueprint('api', __name__)
  api = Api(bp)

  api.add_resource(UserRegister, '/users/register', endpoint='users')

  return bp
