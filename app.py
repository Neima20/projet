from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db, User  # Importez db et vos modèles après avoir créé l'application

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'

# Initialisez db avec l'application Flask
db.init_app(app)




# Créer les tables
with app.app_context():
    db.create_all()
# Importez vos routes après avoir initialisé db pour éviter les importations circulaires
from routes import *

if __name__ == '__main__':
    app.run(debug=True)
