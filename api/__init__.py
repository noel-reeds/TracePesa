from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def fintrack_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fintrack_db.sqlite'
    db.init_app(app)

    from .auth import auth as auth_blueprint
    from .app import app as app_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(app_blueprint)

    return app
