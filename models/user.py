from flask_login import UserMixin
from models.base import Base


class User(UserMixin, db.Model):
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


@app.route('/delete_user', methods=['POST'])
