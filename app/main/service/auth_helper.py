from app.main.model.user import Users


class Auth:
    @staticmethod
    def login_user(data):
        try:
            # fetch the user data
            user = Users.query.filter_by(user_id=data.get('user')).first()
            if user and user.check_password(data.get('password')):
                return 200
            return 401
        except Exception as err:
            print(err)
            return 500
