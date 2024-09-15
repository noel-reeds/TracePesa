from flask import request, flash
from models.storage import User
from api import db
import uuid


class User():
    """User model, defines a user and attrs"""

    def __init__(self, *args, **kwargs):
        """initializes a user object"""
        self.id = str(uuid.uuid4())
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self._password = kwargs.get('_password')
        self.monthly_income = kwargs.get('monthly_income')

    def add_expense(self):
        """Creates an expenditure and adds to the database"""
        expense_id = request.form.get('id')
        new_expense = User.query.filter_by(expense_id)
        
        """Alert user, similar expenditure exists"""
        if new_expense:
            flash('Duplicate expenditure')
        db.session.add(new_expense)
        db.session.commit()


    def remove_expense(self):
        """Deletes an expenditure"""

