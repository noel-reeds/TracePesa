from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


class Expenses(db.Model):
    """attributes of the expenses"""
    id = db.Column(db.Integer, foreign_key=True)
    category = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Expense added to %r>" % self.category


class User(db.Model):
    """contains users of the API"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    income = db.Column(db.Integer, nullable=False)

@app.route('/add_user', methods=['POST'])
def add_user():
    """adds user to users db"""
    user = request.get_json()
    existing_emails = User.query.order_by(User.email).all()
    if user['email'] in existing_emails:
        return 'user already exists'
    new_user = User(username=user['username'], name=user['name'],
                email=['email'], income=user['income'])
    db.session.add(new_user)
    db.session.commit()
    return 'Registration successful'


@app.route('/add_expense', methods=['POST'])
def add_expenses():
    """adds new expenses to the database"""
    expense_data = request.get_json()
    amount = expense_data['amount']
    category = expense_data['category']
    new_expense = Expenses(username=username,
                category=category, name=name, amount=amount)
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
