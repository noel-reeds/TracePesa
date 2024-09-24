from flask import flash, Blueprint, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from . import db, User


auth = Blueprint('auth', __name__)


@auth.route('/login')
def user_login():
    """Logs in a user into the app"""
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login():
    """Redirects successful logins"""
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email).first()

    """Check if user already exists, password check"""
    if user and check_password_hash(user.password, password):
        login_user(user)
        return redirect(url_for('main.profile'))
    
    """if check fails, return to login"""
    flash('Failed, check your credentials and try again')
    return redirect(url_for('auth.user_login')

@auth.route('/signup')
def user_signup():
    """Signs up a user"""
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup():
    """"Adds a user to database"""
    username = request.form.get('username')
    name = request.form.get.get('name')
    password = request.form.get('password')
    email = request.form.get('email')

    user = User.query.filter_by(email).first()
    if user:
        flash("Email already exists, proceed to login")
        return redirect(url_for('auth.user_sign'))

    new_user = User(username=username, name=name, email=email,
            password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()
    
    """Redirect user to login"""
    return redirect(url_for('auth.user_login'))


@auth.route('/logout')
@login_required
def user_logout():
    """Logs out a user"""
    logout_user()
    return redirect(url_for('main.index'))
