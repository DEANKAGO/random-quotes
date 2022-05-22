"""
Creates the app function and returns the app
"""
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate

from config import app_config
from .main.views import main
from .main.models import db, User


def create_app(app_environment):
    """Creates the app instance and returns the app """
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config[app_environment])
    app.register_blueprint(main)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
