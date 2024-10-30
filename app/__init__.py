from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SingletonDB:
    _instance = None

    def __new__(cls, app=None):
        if cls._instance is None:
            cls._instance = super(SingletonDB, cls).__new__(cls)
            cls._instance.init_app(app)
        return cls._instance

    def init_app(self, app):
        if app is not None:
            db.init_app(app)

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    SingletonDB(app)  # Singleton instance of DB

    with app.app_context():
        from models import UserModel, TaskModel
        db.create_all()

    return app