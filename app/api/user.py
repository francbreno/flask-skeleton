from flask_restful import Resource, reqparse
from marshmallow import Schema, fields, pre_load, validate
from ..models.user import UserModel
from .. import ma
from ..repositories.user import save, find_by_username, find_by_id

class UserSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True, validate=validate.Length(2))
    url = ma.URLFor('api.users', id='<id>', _external=True)

class UserRegister(Resource):
    schema = UserSchema()

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type = str,
        required = True,
        help = "The field username cannot be blank."
    )

    parser.add_argument('password',
        type = str,
        required = True,
        help = "The field password cannot be blank."
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if find_by_username(data['username']):
            return { 'message': "A user with that username already exists", 'status_code': 400 }, 400

        save(UserModel(**data))

        return { 'message': "User created successfully", 'status_code': 201 }, 201

    def get(self, id):
        user = find_by_id(id)

        if user:
            return UserRegister.schema.dump(user).data

        return { 'message': "Account not found.", 'status': 404}, 404
