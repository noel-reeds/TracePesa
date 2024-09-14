from flask import Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from . import db # presumably from init..


class Expense(db.Model):
    """attributes of the expenses"""
    id = db.Column(db.Integer, foreign_key=True)
    category = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Expense added to %r>" % self.category


@app.route('/add_expense', methods=['POST'])
def add_expenses():
    """adds new expenses to the database"""
    expense_data = request.get_json()
    amount = expense_data['amount']
    category = expense_data['category']
    name = expense_data['name']
    new_expense = Expenses(category=category, name=name, amount=amount)
    if new_expense.name in Expense.query.order_by(Expense.name).all():
        return 'expenditure already exists'
    db.session.add(new_expense)
    db.session.commit()
    return 'New expense added'

@app.route('/delete_expense/<int:id>', methods=['POST'])
    def delete_expense(id):
        """deletes an expense from the expenses table"""
        expense = Expenses.query.get_or_404(id)
        try:
            db.session.delete(expense)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an err'
