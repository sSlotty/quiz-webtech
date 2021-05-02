from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Foods(db.Model):
    __tablename__ = 'foods'

    name = db.Column(db.String(),primary_key=True)
    Killocalories = db.Column(db.Float())
    Alpha_Carotene = db.Column(db.Float())
    Beta_Carotene = db.Column(db.Float())
    Carbohtdrate = db.Column(db.Float())
    Cholesterol = db.Column(db.Float())
    Choline = db.Column(db.Float())
    Fiber = db.Column(db.Float())
    Lycopene = db.Column(db.Float())
    Manganese = db.Column(db.Float())
    Protein = db.Column(db.Float())
    Zinc = db.Column(db.Float())
    Vitamon_B12 = db.Column(db.Float())
    Vitamin_B6 = db.Column(db.Float())
    Vitamin_C = db.Column(db.Float())
    Vitamin_E = db.Column(db.Float())
    Vitamin_K = db.Column(db.Float())
