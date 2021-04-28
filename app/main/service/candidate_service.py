from app.main import db
from app.main.model.candidate import Candidate
from app.main.utils.db_utils import get_all, save_changes
from app.main.model.user import Users


def save_new_candidate(data):
    candidate = Candidate.query.filter_by(user_id=data['user']).first()
    if not candidate:
        new_candidate = Candidate(
            user_id=data['user'],
            linkedin=data['linkedin'],
            other_webpage=data['other_webpage'],
            bio=data['bio'],
            github=data['github'],
        )
        save_changes(new_candidate)
        response_object = {
            'status': 'success',
            'message': 'Candidate Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Candidate already exists.',
        }
        return response_object, 409


def get_a_candidate(username: str):
    return db.session.query(Candidate, Users).filter(
       Candidate.user_id == Users.user_id).filter(
          Candidate.user_id == username).first()


def get_all_candidate():
    return db.session.query(Candidate, Users).filter(
        Candidate.user_id==Users.user_id).all()
