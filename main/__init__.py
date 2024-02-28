
# Import the necessary modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import DeclarativeBase

from config import Config

# Define your custom base class.
class Base(DeclarativeBase):
    pass

# Initialize SQLAlchemy with the custom base class.
db = SQLAlchemy(model_class=Base)
migrate = Migrate()

def create_app(config_class=Config):
    # Initialize Flask application.
    flask_app = Flask(__name__, template_folder='templates')
    # Load configuration settings from the Config class.
    flask_app.config.from_object(config_class)

    # Initialize SQLAlchemy with the Flask application.
    db.init_app(flask_app)
    # Initialize migration engine with the Flask application and SQLAlchemy instance.
    migrate.init_app(flask_app, db)

    return flask_app

# Import modules at the bottom to avoid circular imports.
from . import models