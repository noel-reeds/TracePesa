from flask import flash, Blueprint, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, User

auth = Blueprint('auth', __name__)

@auth.route('/')
def home_redirect():
    return 'HOME'


@auth.route('/login')
def user_login():
    """Logs in a user into the app"""
    return 'Login'



@auth.route('/signup')
def user_signup():
    """Signs up a user"""
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup():
    """"Adds a user to database"""
    username = request.form.get['username']
    name = request.form.get.get['name']
    password = request.form.get['password']
    email = request.form.get['email']

    user = User.query.filter_by(email).first()
    if user:
        flash("Email already exists, proceed to login")
        return redirect(url_for('auth.user_sign'))

    new_user = User(username=username, name=name, email=email,
            password=generate_password_hash(password, method='sha256'))
    db.session.commit()
    
    """Redirect user to login"""
    return redirect(url_for('auth.user_login'))


@auth.route('/logout')
def user_logout():
    """logs out a user"""
    return 'Logout'
