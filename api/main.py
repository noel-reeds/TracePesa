from flask import Blueprint


home = Blueprint('main', __name__)

@home.route('/')
def index():
    """Returns index page"""
    return 'Index'


@home.route('/profile')
def profile():
    """Returns a logged in user"""
    return 'Profile'
