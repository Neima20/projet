# create_db.py

from app import app, db
from models import User, Post

# Initialise l'application Flask pour que la base de données soit créée
with app.app_context():
    db.create_all()
