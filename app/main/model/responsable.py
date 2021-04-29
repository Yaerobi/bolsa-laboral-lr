from app.main import db


class Responsable(db.Model):
    __tablename__ = 'responsable'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    user_id = db.Column(db.String(255), db.ForeignKey('users.user_id'),
                        nullable=False)

    company_id = db.Column(db.Integer, db.ForeignKey('company.id'),
                           nullable=True)
    company = db.relationship("Company", back_populates="responsable")



