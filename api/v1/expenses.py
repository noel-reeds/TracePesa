from flask import Flask, Blueprint, request, jsonify
from models.expense import Expense
from models.user import User
from app import db
from datetime import datetime, date

expense = Blueprint('expense', __name__)

@expense.route('/api/v1/expense/add/<int:user_id>', methods=['POST'])
def add_expense(user_id):
    """Adds an expenditure to the database"""
    expense_info = request.json
    category = expense_info.get('category')
    desc = expense_info.get('desc')
    name = expense_info.get('name')
    amount = expense_info.get('amount')
    current_date = date.today()
    
    # check if user exists before expense persists
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({'message': 'user does not exist'})
    new_expense = Expense(user_id=user_id,category=category, desc=desc,
            name=name, amount=amount, date=current_date)
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({'message': 'expense add success'})


@expense.route('/api/v1/expense/remove/<int:expense_id>', methods=['POST'])
def remove_expense(expense_id):
    """Deletes an expense from database"""
    req_data = request.json
    user_id = req_data.get('user_id')
    expense = Expense.query.filter_by(id=expense_id, user_id=user_id).all()
    #check if expense exists
    if expense:
        for obj in expense:
            db.session.delete(obj)
        db.session.commit()
        return jsonify({'message': 'expense delete success'})
    return jsonify({'message': 'expense does not exist'})

@expense.route('/api/v1/expenses/<int:user_id>', methods=['GET'])
def expenses(user_id):
    """returns all expenses of a user"""
    if not User.query.filter_by(id=user_id).first():
        return jsonify({'message': 'user does not exist'})
    expenses = Expense.query.filter_by(user_id=user_id).all()
    if expenses:
        return jsonify([expense.to_dict() for expense in expenses])
    return jsonify({'message': 'no expenses for this period'})


@expense.route('/expense/update/<int:expense_id>', methods=['PUT'])
def update_expense(expense_id):
    """Updates a user expenditure"""
    expense = Expense.query.filter_by(id=expense_id, user_id=user_id).first()
    try:
        expense_info = request.get_json()
        expense.amount = expense_info.get('amount')
        expense.name = expense_info.get('name')
        expense.desc = expense_info.get('desc')
        expense.date = datetime.strptime(expense_info.get('date'), '%Y-%m-%d')

        db.session.commit()
    except:
        return jsonify({'message': 'Error occured updating expenditure'})
