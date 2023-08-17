from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task_calendar.db'
db = SQLAlchemy(app)

from task_calendar_app import routes

# Import your models after defining the db object
from task_calendar_app import models

# Create the database tables within the application context
with app.app_context():
    db.create_all()
