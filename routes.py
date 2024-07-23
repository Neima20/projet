from flask import render_template, request, redirect, url_for, flash, session
from app import app, db
from models import User

# Route pour la page de connexion
@app.route('/')
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
                return redirect(url_for('index'))  # Redirige vers 'index' après la connexion
            else:
                flash('Mot de passe incorrect!', 'error')
        else:
            flash('Utilisateur non trouvé! Veuillez vous inscrire.', 'error')
            return redirect(url_for('inscription'))  # Redirige vers la page d'inscription
    
    return render_template('html/PageConnexion.html', title='Connexion')

# Route pour la page d'inscription
@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

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
            return redirect(url_for('login'))  # Redirige vers 'login' après l'inscription
    
    return render_template('html/Inscription.html', title='Inscription')

# Route pour la page d'accueil après la connexion
@app.route('/index')
def index():
    # Vérifiez si l'utilisateur est connecté en vérifiant la session
    if 'user_id' in session:
        user_id = session['user_id']
        # Récupérer les informations de l'utilisateur connecté depuis la base de données si nécessaire
        user = User.query.get(user_id)
        return render_template('html/Index.html', title='Accueil', user=user)
    else:
        # Rediriger vers la page de connexion si l'utilisateur n'est pas connecté
        flash('Veuillez vous connecter pour accéder à cette page.', 'error')
        return redirect(url_for('login'))
