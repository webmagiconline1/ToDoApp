# filepath: todoapp/app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

db = SQLAlchemy()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['RECAPTCHA_PUBLIC_KEY'] = 'your_public_key'
    app.config['RECAPTCHA_PRIVATE_KEY'] = 'your_private_key'

    db.init_app(app)
    csrf.init_app(app)

    with app.app_context():
        from . import views
        db.create_all()

    return app