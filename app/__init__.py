from flask import Flask
from app.config import Config 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.login_message_category = 'info'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    login_manager.init_app(app)

    from app.routes.main import main
    app.register_blueprint(main)
    from app.routes.admin import admin
    app.register_blueprint(admin)

    return app
