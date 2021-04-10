import datetime

from app.main import db
from app.main.model.candidate import Candidate
from typing import List
from app.main.utils.db_utils import get_all, save_changes


def save_new_candidate(data):
    candidate = Candidate.query.filter_by(email=data['email']).first()
    if not candidate:
        new_candidate = Candidate(
            user_id=data['user_id'],
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
    return Candidate.query.filter_by(user_id=username).first()


def get_all_candidate():
    return get_all(Candidate)

