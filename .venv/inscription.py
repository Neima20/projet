from flask import Flask, render_template, session, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'

# Initialisez db avec l'application mais ne liez pas encore l'application
db = SQLAlchemy()

# Liez db à l'application Flask après les imports pour éviter l'import circulaire
db.init_app(app)

# Importez les blueprints des pages d'inscription et de connexion
from inscription import inscription_bp
from connexion import connexion_bp

# Enregistrez les blueprints avec l'application
app.register_blueprint(inscription_bp)
app.register_blueprint(connexion_bp)

# Définissez vos routes Flask ci-dessous
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

