from app.main import db


class Technologies(db.Model):
    __tablename__ = 'Technologies'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(25), nullable=False)

    # TODO: FIX the logic here
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
    #                     nullable=False)
