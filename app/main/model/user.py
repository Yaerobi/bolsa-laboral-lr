from app.main import db
from app.main import flask_bcrypt

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(100))
    register_on = db.Column(db.DateTime, nullable=False)
    last_pass_change = db.Column(db.DateTime, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)

    country_city_id = db.Column(db.Integer, db.ForeignKey('countries_cities.id'),
                                nullable=False)

    technologies = db.relationship('Technologies', backref=db.backref('techs',
                                                                      lazy=True))
    @property
    def password(self):
        raise AttributeError("password: write-only field")

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__ (self):
        return f"<Person '{self.name} {self.surname} - {self.email}"

