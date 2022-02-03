from flask import Flask
from config import Config

#SQL ALCHEMY IMPORTS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app= Flask(__name__)
app.config.from_object(Config)
# DB inits
db= SQLAlchemy(app)
migrate= Migrate(app,db)

from app import routes, models
