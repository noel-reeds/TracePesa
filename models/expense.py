from app import db
from datetime import datetime


class Expense(db.Model):
    """Entails details of an expenditure"""

    __tablename__ = 'expenses'

    id = db.Column(db.Integer(50), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_id'), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Integer(50), nullable=False)
    date = db.Column(db.datetime, nullable=False)
    
    def expense_to_dict(self):
        """Returns a dictionary of the expense"""
        return {
            'id': self.id,
            'category': self.category,
            'desc': self.desc,
            'name': self.name,
            'amount': self.amount,
            'date': self.date.strptime('%Y-%m-%d')
        }
