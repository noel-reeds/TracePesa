from flask import Blueprint, render_template
from flask_login import login_required, current_user


main = Blueprint('main', __name__)

@main.route('/')
def index():
    """Returns index page"""
    return 'Index'


@main.route('/profile')
@login_required
def profile():
    """Returns a logged in user"""
    return render_template('profile.html', name=current_user.name)
