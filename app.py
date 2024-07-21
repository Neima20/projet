from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from models import User, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'

# Initialisez db avec l'application mais ne liez pas encore l'application
db = SQLAlchemy()

# Liez db à l'application Flask après les imports pour éviter l'import circulaire
db.init_app(app)

# Définissez vos routes Flask ci-dessous

@app.route('/')
def connexion():
    return render_template('/templates/html/PageConnexion.html')

@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']

        # Vérifier si l'utilisateur existe déjà
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Cet email est déjà utilisé. Veuillez utiliser un autre email.', 'error')
        elif password != confirm_password:
            flash('Les mots de passe ne correspondent pas.', 'error')
        else:
            # Créer un nouvel utilisateur
            new_user = User(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash('Vous êtes inscrit avec succès! Connectez-vous maintenant.', 'success')
            return redirect(url_for('login'))
    
    return render_template('/templates/html/Inscription.html' title='Inscription')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Récupérer l'utilisateur correspondant à l'email fourni
        user = User.query.filter_by(email=email).first()
        if user:
            # Vérifier si le mot de passe correspond
            if user.password == password:
                flash('Vous êtes connecté!', 'success')
                # Stocker l'ID de l'utilisateur dans la session
                session['user_id'] = user.id
                return redirect(url_for('index'))
            else:
                flash('Mot de passe incorrect!', 'error')
        else:
            flash('Utilisateur non trouvé!', 'error')       
    
    return render_template('templates/html/PageConnexion.html', title='Connexion')

if __name__ == '__main__':
    app.run(debug=True)
