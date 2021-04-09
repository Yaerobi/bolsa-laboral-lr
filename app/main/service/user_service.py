import datetime

from app.main import db
from app.main.model.user import Users
from app.main.model.technologies import Technologies
from typing import List


def save_new_user(data):
    user = Users.query.filter_by(email=data['email']).first()
    if not user:
        new_user = Users(
            user_id=data['user'],
            password_hash=data['password'],
            register_on=datetime.datetime.utcnow(),
            last_pass_change=datetime.datetime.utcnow(),
            name=data['name'],
            surname=data['surname'],
            email=data['email'],
            country_city_id=data['country_city_id'],
        )
        # TODO: Fix this in the future
        # save_technologies(new_user, data['technologies'])
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def save_technologies(user: Users, technologies_list: List):
    for tech in technologies_list:
        technology = Technologies.query.filter_by(id=tech)
        user.technologies.append(technology)


def get_all_users():
    return Users.query.all()


def get_a_user(username: str):
    return Users.query.filter_by(user_id=username).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
