from . import db

class User(db.Model):
    """User model, defines a user and attrs"""

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    # establish a relation between the user and expense table
    return '<user {}>'.format(self.username)
