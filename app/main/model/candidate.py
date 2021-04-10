from app.main import db

class Candidate(db.Model):
    __tablename__ = 'candidate'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    linkedin = db.Column(db.String(255), nullable=True)
    other_webpage = db.Column(db.String(255), nullable=True)
    bio = db.Column(db.String(255), unique=True, nullable=False)
    github = db.Column(db.String(255), nullable=True)

    user_id = db.Column(db.String(255), db.ForeignKey('users.user_id'),
                        nullable=False)
