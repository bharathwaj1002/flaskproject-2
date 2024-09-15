from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)

    from .views import views  # Import the Blueprint
    app.register_blueprint(views)  # Register the Blueprint

    with app.app_context():
        db.create_all()  # Create database tables for our data models

    return app