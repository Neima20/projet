from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# Créer une instance de SQLAlchemy
db = SQLAlchemy()
migrate = Migrate()
def create_app():
    # Créer une instance de Flask
    app = Flask(__name__)
    
    # Configurer la base de données
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
    app.config['SECRET_KEY'] = 'your_secret_key'  # Assurez-vous de définir une clé secrète pour les sessions
    
    # Initialiser SQLAlchemy avec l'application
    db.init_app(app)
    migrate.init_app(app, db)  # Initialiser Flask-Migrate avec l'application et SQLAlchemy
    # Importer les routes après avoir configuré l'application
    with app.app_context():
        from . import routes
        routes.register_routes(app)  # Enregistrer les routes avec l'application
    
    return app
