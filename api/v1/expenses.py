from flask import Flask, Blueprint, request, jsonify
from models.expense import Expense
from app import db
from datetime import datetime

expense = Blueprint('expense', __name__)

@expense.route('/api/v1/expense/add', methods=['POST'])
def add_expense():
    """Adds an expenditure to the database"""
    expense_info = request.json
    category = expense_info.get('category')
    desc = expense_info.get('desc')
    name = expense_info.get('name')
    amount = expense_info.get('amount')
    date = datetime.strptime(datetime.utcnow(), '%Y-%m-%d')

    new_expense = Expense(user_id=user_id, category=category, desc=desc,
            name=name, amount=amount, date=date)
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({'message': 'Expense added successfully'})


@expense.route('/expense/remove/int:expense_id>', methods=['POST'])
def remove_expense(expense_id):
    """Deletes an expense from database"""
    expense = Expense.query.get_or_404(expense_id)
    
    try:
        db.session.delete(expense)
        db.session.commit()
        return jsonify({'message': 'Expense deleted successfully'})

    except:
        return jsonify({'message': 'Expense does not exist'})

@expense.route('/expense/get_expenses/<int:user_id>', methods=['GET'])
def get_expenses(user_id):
    """returns all expenses of a user"""
    expenses = Expense.query.filter_by(user_id).all()
    
    try:
        return jsonify({expense.expense_to_dict() for expense in expenses})

    except:
        return jsonify({'message': 'No expenses for the user, add some!'})


@expense.route('/expense/update/<int:expense_id>', methods=['PUT'])
def update_expense(expense_id):
    """Updates a user expenditure"""
    expense = Expense.query.get_or_404(expense_id)
    try:
        expense_info = request.get_json()
        expense.amount = expense_info.get('amount')
        expense.name = expense_info.get('name')
        expense.desc = expense_info.get('desc')
        expense.date = datetime.strptime(expense_info.get('date'), '%Y-%m-%d')

        db.session.commit()
    except:
        return jsonify({'message': 'Error occured updating expenditure'})
