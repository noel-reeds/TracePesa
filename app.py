from flask import Flask
import os
from flask_login import LoginManager
from models import db


def fintrack_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fintrack_db.sqlite'
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view ='auth.login'
    login_manager.init_app(app)

    from models.user import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from api.v1.auth import auth as auth_blueprint
    from api.v1.main import main as main_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)

    return app


if __name__ == "__main__":
    app = fintrack_app()
    app.run(debug=True)
