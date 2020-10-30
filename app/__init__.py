from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
import os

#app = Flask(__name__)
#app.config.from_pyfile('config.py')

# Flask und Config initialisieren
app = Flask(__name__, instance_relative_config=False)
config = app.config.from_object('config.DevelopmentConfig')

# Datenbank initialisieren
db = SQLAlchemy(app)

# Marshmallow initialisieren
ma = Marshmallow(app)

migrate = Migrate(app, db)

from . import routes, models