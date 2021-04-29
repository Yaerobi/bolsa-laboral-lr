from app.main import db
from app.main.model.responsable import Responsable
from app.main.utils.db_utils import save_changes
from app.main.model.user import Users


def save_new_responsable(data):
    candidate = Responsable.query.filter_by(user_id=data['user']).first()
    if not candidate:
        new_responsable = Responsable(
            user_id=data['user'],
            company_id=data['company_id']
        )
        save_changes(new_responsable)
        response_object = {
            'status': 'success',
            'message': 'Responsable Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Responsable already exists.',
        }
        return response_object, 409


def get_a_responsable(username: str):
    return db.session.query(Responsable, Users).filter(
       Responsable.user_id == Users.user_id).filter(
          Responsable.user_id == username).first()


def get_all_responsable():
    return db.session.query(Responsable, Users).filter(
        Responsable.user_id == Users.user_id).all()
