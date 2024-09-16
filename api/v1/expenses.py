from flask import Flask, Blueprint
from models.expense import Expense

expense = Blueprint('expense', __name__)

@expense.route(
