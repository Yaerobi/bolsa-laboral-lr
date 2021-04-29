import datetime

from flask_testing import TestCase

from manage import app, db

from app.main.service.responsable_service import (
    save_new_responsable,
    get_all_responsable,
    get_a_responsable,
)
from app.main.model.user import Users
from app.main.model.responsable import Responsable


class TestResponsableServices(TestCase):
    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')
        return app

    def test_save_new_responsable(self):
        data = dict()
        data['user'] = 'eamanu'
        data['company_id'] = 'test'

        save_new_responsable(data)

        responsable_result = Responsable.query.filter_by(user_id='eamanu').first()

        self.assertEqual('eamanu', responsable_result.user_id)

    def test_get_all_candidate(self):
        self.assertEqual([], get_all_responsable())

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
        responsable1 = Responsable(
            user_id='eamanu',
            company_id='1',
        )

        responsable2 = Responsable(
            user_id='eamanu2',
            company_id='1'
        )

        db.session.add(user1)
        db.session.add(user2)

        db.session.add(responsable1)
        db.session.add(responsable2)

        db.session.commit()

        all_responsable = get_all_responsable()

        self.assertEqual(2, len(all_responsable))
        for respon, user in all_responsable:
            self.assertIn(f'eamanu', user.user_id)
            self.assertEqual(1, respon.company_id)

    def test_get_a_responsable(self):
        self.assertEqual([], get_all_responsable())

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

        responsable1 = Responsable(
            user_id='eamanu',
            company_id='1',
        )

        responsable2 = Responsable(
            user_id='eamanu2',
            company_id='1'
        )

        db.session.add(user1)
        db.session.add(user2)

        db.session.add(responsable1)
        db.session.add(responsable2)

        db.session.commit()

        candidate, user = get_a_responsable('eamanu')

        self.assertEqual('Emmanuel', user.name)
        self.assertEqual('Arias', user.surname)
        self.assertEqual('eamanu@yaerobi', user.email)
        self.assertEqual('hola', user.password_hash)
        self.assertEqual(1, candidate.company_id)
        self.assertEqual('eamanu', candidate.user_id)

    def test_response_409_if_already_exist_candidate(self):
        self.assertEqual([], get_all_responsable())

        data = dict()
        data['user'] = 'eamanu'
        data['company_id'] = '1'

        response, code_status = save_new_responsable(data)

        response_object = {
            'status': 'success',
            'message': 'Responsable Successfully registered.'
        }
        self.assertEqual(response_object, response)
        self.assertEqual(201, code_status)

        data = dict()
        data['user'] = 'eamanu'
        data['company_id'] = '2'

        response, code_status = save_new_responsable(data)

        response_object = {
            'status': 'fail',
            'message': 'Responsable already exists.'
        }

        self.assertEqual(response_object, response)
        self.assertEqual(409, code_status)
