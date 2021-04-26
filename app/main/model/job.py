from app.main import db


class Job(db.Model):
    __tablename__ = 'job'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    start = db.Column(db.DateTime, nullable=False)
    closing = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(25), nullable=False)

    company_id = db.Column(db.Integer, db.ForeignKey('company.id'),
                           nullable=True)
    company = db.relationship("Company", back_populates="job")