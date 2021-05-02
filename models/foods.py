from flask_sqlalchemy import SQLAlchemy
from app import db

class Foods(db.Model):
    __tablename__ = 'foods'

    name = db.Column(db.String(),unique=True)
    Killocalories = db.Column(db.Number())
    Alpha-Carotene = db.Column(db.Number())
    Beta-Carotene = db.Column(db.Number())
    Carbohtdrate = db.Column(db.Number())
    Cholesterol = db.Column(db.Number())
    Choline = db.Column(db.Number())
    Fiber = db.Column(db.Number())
    Lycopene = db.Column(db.Number())
    Manganese = db.Column(db.Number())
    Protein = db.Column(db.Number())
    Zinc = db.Column(db.Number())
    Vitamon-B12 = db.Column(db.Number())
    Vitamin-B6 = db.Column(db.Number())
    Vitamin-C = db.Column(db.Number())
    Vitamin-E = db.Column(db.Number())
    Vitamin-K = db.Column(db.Number())
