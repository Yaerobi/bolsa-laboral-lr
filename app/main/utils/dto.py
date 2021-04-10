from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'name': fields.String(required=True, description='user name'),
        'surname': fields.String(required=True, description='user surname'),
        'password': fields.String(required=True, description='user password'),
        'user_id': fields.String(description='user Identifier'),
        'country_city_id': fields.String(description='Countr and city')
    })
