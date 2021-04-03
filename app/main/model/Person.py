from  app.main import db


class Persons(db.Model):
    __tablename__ = 'persons'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullabe=False)
    provincia = db.Column(db.String(255), nullable=False)
    ciudad = db.Column(db.String(255), nullable=True)

    def __repr__ (self):
        return f"<Person '{self.name} {self.surname} - {self.email}"

