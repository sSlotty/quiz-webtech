from flask_sqlalchemy import SQLAlchemy
from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(),unique=True)
    password = db.Column(db.String())

    def __repr__(self):
        return f"{self.name}"