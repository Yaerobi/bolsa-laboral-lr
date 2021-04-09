import os
import unittest

from flask import current_app
from flask_testing import TestCase

from manage import app
from app.main.config import basedir
from app.main.service.user_service import save_new_user
from app.main.model.user import Users

class TestUserServices(TestCase):
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
        data['technologies'] = '1,2,3'

        save_new_user(data)

        user_result = Users.query.filter_by(user_id='eamanu').first()

        self.assertEqual('eamanu', user_result.user_id)

if __name__ == '__main__':
    unittest.main()
