import unittest
import datetime

from flask_testing import TestCase

from manage import app, db
from app.main.service.user_service import (
    save_new_user,
    get_all_users,
    get_a_user,
)
from app.main.service.candidate_service import (
    save_new_candidate,
    get_all_candidate,
    get_a_candidate,
)
from app.main.model.user import Users
from app.main.model.candidate import Candidate


class TestUserServices(TestCase):
    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')
        return app

    def test_save_new_user(self):
        data = dict()
        data['user'] = 'eamanu'
        data['password'] = 'hola'
        data['name'] = 'Emmanuel'
        data['surname'] = 'Arias'
        data['email'] = 'eamanu@yaerobi.com'
        data['country_city_id'] = '1'

        save_new_user(data)

        user_result = Users.query.filter_by(user_id='eamanu').first()

        self.assertEqual('eamanu', user_result.user_id)

    def test_get_all_users(self):
        self.assertEqual([], get_all_users())

        user1 = Users(
            user_id='eamanu',
            password_hash='hola',
            register_on=datetime.datetime.utcnow(),
            last_pass_change=datetime.datetime.utcnow(),
            name='Emmanuel',
            surname='Arias',
            email='eamanu@yaerobi',
            country_city_id='1',
        )
        user2 = Users(
            user_id='eamanu2',
            password_hash='hola',
            register_on=datetime.datetime.utcnow(),
            last_pass_change=datetime.datetime.utcnow(),
            name='Emmanuel',
            surname='Arias',
            email='eamanu2@yaerobi',
            country_city_id='1',
        )

        user3 = Users(
            user_id='eamanu3',
            password_hash='hola',
            register_on=datetime.datetime.utcnow(),
            last_pass_change=datetime.datetime.utcnow(),
            name='Emmanuel',
            surname='Arias',
            email='eamanu3@yaerobi',
            country_city_id='1',
        )
        db.session.add(user1)
        db.session.add(user2)
        db.session.add(user3)

        db.session.commit()

        all_users = get_all_users()

        self.assertEqual(3, len(all_users))
        for user in all_users:
            self.assertEqual('Emmanuel', user.name)
            self.assertEqual('Arias', user.surname)

    def test_get_a_user(self):
        self.assertEqual([], get_all_users())

        user1 = Users(
            user_id='eamanu',
            password_hash='hola',
            register_on=datetime.datetime.utcnow(),
            last_pass_change=datetime.datetime.utcnow(),
            name='Emmanuel',
            surname='Arias',
            email='eamanu@yaerobi',
            country_city_id='1',
        )
        user2 = Users(
            user_id='eamanu2',
            password_hash='hola',
            register_on=datetime.datetime.utcnow(),
            last_pass_change=datetime.datetime.utcnow(),
            name='Emmanuel',
            surname='Arias',
            email='eamanu2@yaerobi',
            country_city_id='1',
        )

        user3 = Users(
            user_id='eamanu3',
            password_hash='hola',
            register_on=datetime.datetime.utcnow(),
            last_pass_change=datetime.datetime.utcnow(),
            name='Emmanuel',
            surname='Arias',
            email='eamanu3@yaerobi',
            country_city_id='1',
        )
        db.session.add(user1)
        db.session.add(user2)
        db.session.add(user3)

        db.session.commit()

        user = get_a_user('eamanu')
        self.assertEqual('Emmanuel', user.name)
        self.assertEqual('Arias', user.surname)
        self.assertEqual('eamanu@yaerobi', user.email)
        self.assertEqual('hola', user.password_hash)

    def test_response_409_if_already_exist_user(self):
        self.assertEqual([], get_all_users())

        data = dict()
        data['user'] = 'eamanu'
        data['password'] = 'hola'
        data['name'] = 'Emmanuel'
        data['surname'] = 'Arias'
        data['email'] = 'eamanu@yaerobi.com'
        data['country_city_id'] = '1'

        response, code_status = save_new_user(data)

        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        self.assertEqual(response_object, response)
        self.assertEqual(201, code_status)

        data = dict()
        data['user'] = 'eamanu'
        data['password'] = 'hola'
        data['name'] = 'Emmanuel'
        data['surname'] = 'Arias'
        data['email'] = 'eamanu@yaerobi.com'
        data['country_city_id'] = '1'

        response, code_status = save_new_user(data)

        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.'
        }
        self.assertEqual(response_object, response)
        self.assertEqual(409, code_status)


if __name__ == '__main__':
    unittest.main()
