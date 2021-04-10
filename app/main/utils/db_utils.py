from app.main import db


def get_all(data):
    return data.query.all()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
