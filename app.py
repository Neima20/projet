from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'

# Initialisation de SQLAlchemy avec l'application
db = SQLAlchemy(app)

# Importation des routes après l'initialisation de db
from routes import *

# Créer les tables
with app.app_context():
    db.create_all()

