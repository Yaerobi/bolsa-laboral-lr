from app.main import db

class CountriesCities(db.Model):
    __tablename__ = 'countries_cities'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country = db.Column(db.String(255), nullable=False)
    province = db.Column(db.String(255), nullable=False)
