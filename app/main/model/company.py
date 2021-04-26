from app.main import db


class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    responsable = db.relationship("Responsable", back_populates="company")
    job = db.relationship("Job", back_populates="job")



