import datetime

from flask import (request, jsonify)
from flask_restplus import Resource
from flask_jwt_extended import (create_access_token, get_jwt_identity)

from app.main.service.auth_helper import Auth
from app.main.utils.dto import AuthDto

api = AuthDto.api
user_auth = AuthDto.user_auth

EXPIRE_TOKEN = datetime.timedelta(hours=24)

@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        code = Auth.login_user(data=post_data)
        if code == 200:
            access_token = create_access_token(identity=post_data.get('user'), expires_delta=EXPIRE_TOKEN)
            # TODO: jsonnify seems does not work with flask_restplus
            # analize the best way to return the "access_token"
            return jsonify(access_token=access_token)
        elif code == 401:
            return {
                       'status': 'fail',
                       'message': "Bad username or password"
                   }, 401
        else:
            return {
                       'status': 'fail',
                       "msg": "Internal error. Piece of Cake"
                   }, 500


@api.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a user')
    def get(self):
        current_user = get_jwt_identity()
        # TODO: Save token on the Database
        return jsonify({"msg": f"Bye Bye {current_user}"}), 200
