from flask import render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
from models import User
from models import Category
from forms import CategoryForm

# Route pour la page de connexion
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Récupérer l'utilisateur correspondant à l'email fourni
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            flash('Vous êtes connecté!', 'success')
            # Stocker l'ID de l'utilisateur dans la session
            session['user_id'] = user.id
            return redirect(url_for('tableau'))  # Redirige vers 'tableau' après la connexion
        else:
            flash('Email ou mot de passe incorrect!', 'error')
    
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
            # Créer un nouvel utilisateur avec un mot de passe haché
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            new_user = User(username=username, email=email, password=hashed_password)
            try:
                db.session.add(new_user)
                db.session.commit()
                flash('Vous êtes inscrit avec succès! Connectez-vous maintenant.', 'success')
                return redirect(url_for('login'))  # Redirige vers 'login' après l'inscription
            except Exception as e:
                flash('Erreur lors de l\'inscription. Veuillez réessayer.', 'error')
                print(f"Erreur : {e}")
    
    return render_template('html/Inscription.html', title='Inscription')

# Route pour la page d'accueil après la connexion
@app.route('/tableau')
def tableau():
    # Vérifiez si l'utilisateur est connecté en vérifiant la session
    if 'user_id' in session:
        user_id = session['user_id']
        # Récupérer les informations de l'utilisateur connecté depuis la base de données si nécessaire
        user = User.query.get(user_id)
        return render_template('html/tableau.html', title='table', user=user)
    else:
        # Rediriger vers la page de connexion si l'utilisateur n'est pas connecté
        flash('Veuillez vous connecter pour accéder à cette page.', 'error')
        return redirect(url_for('login'))

@app.route('/categorie')
def categorie():
    # Vérifiez si l'utilisateur est connecté en vérifiant la session
    if 'user_id' in session:
        user_id = session['user_id']
        # Récupérer les informations de l'utilisateur connecté depuis la base de données si nécessaire
        user = User.query.get(user_id)
        return render_template('html/categorie.html', title='categorie', user=user)
    else:
        # Rediriger vers la page de connexion si l'utilisateur n'est pas connecté
        flash('Veuillez vous connecter pour accéder à cette page.', 'error')
        return redirect(url_for('login'))

@app.route('/tache')
def tache():
        # Vérifiez si l'utilisateur est connecté en vérifiant la session
    if 'user_id' in session:
        user_id = session['user_id']
        # Récupérer les informations de l'utilisateur connecté depuis la base de données si nécessaire
        user = User.query.get(user_id)
        return render_template('html/tache.html', title='Tache', user=user)
    else:
        # Rediriger vers la page de connexion si l'utilisateur n'est pas connecté
        flash('Veuillez vous connecter pour accéder à cette page.', 'error')
        return redirect(url_for('login'))

@app.route('/rappel')
def rappel():
          # Vérifiez si l'utilisateur est connecté en vérifiant la session
    if 'user_id' in session:
        user_id = session['user_id']
        # Récupérer les informations de l'utilisateur connecté depuis la base de données si nécessaire
        user = User.query.get(user_id)
        return render_template('html/rappel.html', title='rappel', user=user)
    else:
        # Rediriger vers la page de connexion si l'utilisateur n'est pas connecté
        flash('Veuillez vous connecter pour accéder à cette page.', 'error')
        return redirect(url_for('login'))
    
@app.route('/calendrier')
def calendrier():
          # Vérifiez si l'utilisateur est connecté en vérifiant la session
    if 'user_id' in session:
        user_id = session['user_id']
        # Récupérer les informations de l'utilisateur connecté depuis la base de données si nécessaire
        user = User.query.get(user_id)
        return render_template('html/calendrier.html', title='calendrier', user=user)
    else:
        # Rediriger vers la page de connexion si l'utilisateur n'est pas connecté
        flash('Veuillez vous connecter pour accéder à cette page.', 'error')
        return redirect(url_for('login'))

@app.route('/aide')
def aide():
          # Vérifiez si l'utilisateur est connecté en vérifiant la session
    if 'user_id' in session:
        user_id = session['user_id']
        # Récupérer les informations de l'utilisateur connecté depuis la base de données si nécessaire
        user = User.query.get(user_id)
        return render_template('html/aide.html', title='aide', user=user)
    else:
        # Rediriger vers la page de connexion si l'utilisateur n'est pas connecté
        flash('Veuillez vous connecter pour accéder à cette page.', 'error')
        return redirect(url_for('login'))

@app.route('/parametre')
def parametre():
           # Vérifiez si l'utilisateur est connecté en vérifiant la session
    if 'user_id' in session:
        user_id = session['user_id']
        # Récupérer les informations de l'utilisateur connecté depuis la base de données si nécessaire
        user = User.query.get(user_id)
        return render_template('html/parametre.html', title='parametre', user=user)
    else:
        # Rediriger vers la page de connexion si l'utilisateur n'est pas connecté
        flash('Veuillez vous connecter pour accéder à cette page.', 'error')
        return redirect(url_for('login'))


# Ajouter UN CATEGORIE:

@app.route('/categories', methods=['GET', 'POST'])
def categories():
    form = CategoryForm()
    if form.validate_on_submit():
        category_name = form.name.data
        new_category = Category(name=category_name)
        db.session.add(new_category)
        db.session.commit()
        flash('Categorie ajoute avec sucess!', 'success')
        return redirect(url_for('categories'))
    
    categories = Category.query.all()
    return render_template('html/AjouterCategorie.html', form=form, categories=categories)