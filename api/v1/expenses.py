from flask import Flask, Blueprint, request, datetime, jsonify
from models.expense import Expense
from app import db

expense = Blueprint('expense', __name__)

@expense.route('expense/add', methods=['POST'])
def add_expense():
    """Adds an expenditure to the database"""
    expense_info = request.get_json()
    user_id = expense_info.get('user_id')
    category = expense_info.get('category')
    desc = expense_info.get('desc')
    name = expense.info.get('name')
    amount = expense_info.get('amount')
    date = datetime.strptime(expense_info.get('date'), '%Y-%m-%d')

    new_expense = Expense(user_id=user_id, category=category, desc=desc,
            name=name, amount=amount, date=date)
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({'message': 'Expense added successfully'})


@expense.route('expense/remove/int:expense_id>', methods=['POST'])
def remove_expense(expense_id):
    """Deletes an expense from database"""
    expense = Expense.query.get_or_404(expense_id)
    
    try:
        db.session.delete(expense)
        db.session.commit()
        return jsonify({'message': 'Expense deleted successfully'})

    except:
        return jsonify({'message': 'Expense does not exist'})

