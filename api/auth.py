from flask import Blueprint, render_template, request
from . import db, User

auth = Blueprint('auth', __name__)

@auth.route('/')
def home_redirect():
    return 'HOME'


@auth.route('/login')
def user_login():
    """logs in a user into the app"""
    return 'Login'



@auth.route('/signup')
def user_signup():
    """signs up a user"""
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup():
    """"adds a user to database"""
    username = request.form.get['username']
    name = request.form.get.get['name']
    password = request.form.get['password']
    email = request.form.get['email']

    user = User.query.filter_by(email).first()
    if user:
        return redirect(url_for('auth.user_sign'))

    new_user = User(username=username, name=name, email=email)
    db.session.add(new_user)
    db.session.commit()
    
    """redirect user to login"""
    return redirect(url_for('auth.user_login'))


@auth.route('/logout')
def user_logout():
    """logs out a user"""
    return 'Logout'
