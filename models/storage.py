from flask_login import UserMixin
from api import db


class User(UserMixin, db.Model):
    """Contains users of the API"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    income = db.Column(db.Integer, nullable=False)

class Expense(db.Model):
    """Entails details of an expenditure"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Integer(50), nullable=False)
    created = db.Column(db.datetime, nullable=False)
