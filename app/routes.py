from flask import render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User, Category, Task
from .forms import CategoryForm, EditCategoryForm, DeleteCategoryForm, TaskForm


# Route pour la page de connexion
def register_routes(app):
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
        if 'user_id' in session:
            user_id = session['user_id']
            user = User.query.get(user_id)
            return render_template('html/tableau.html', title='table', user=user)
        else:
            flash('Veuillez vous connecter pour accéder à cette page.', 'error')
            return redirect(url_for('login'))

    @app.route('/categorie')
    def categorie():
        if 'user_id' in session:
            user_id = session['user_id']
            user = User.query.get(user_id)
            categories = Category.query.filter_by(user_id=user_id).all()
            return render_template('html/categorie.html', title='categorie', user=user, categories=categories)
        else:
            flash('Veuillez vous connecter pour accéder à cette page.', 'error')
            return redirect(url_for('login'))

    @app.route('/tache')
    def tache():
        if 'user_id' in session:
            user_id = session['user_id']
            user = User.query.get(user_id)
            tasks = Task.query.filter_by(user_id=user_id).all()  # Récupérer les tâches associées à l'utilisateur
            return render_template('html/tache.html', title='Tache', user=user, tasks=tasks)
        else:
            flash('Veuillez vous connecter pour accéder à cette page.', 'error')
            return redirect(url_for('login'))

    @app.route('/rappel')
    def rappel():
        if 'user_id' in session:
            user_id = session['user_id']
            user = User.query.get(user_id)
            return render_template('html/rappel.html', title='rappel', user=user)
        else:
            flash('Veuillez vous connecter pour accéder à cette page.', 'error')
            return redirect(url_for('login'))

    @app.route('/calendrier')
    def calendrier():
        if 'user_id' in session:
            user_id = session['user_id']
            user = User.query.get(user_id)
            return render_template('html/calendrier.html', title='calendrier', user=user)
        else:
            flash('Veuillez vous connecter pour accéder à cette page.', 'error')
            return redirect(url_for('login'))

    @app.route('/aide')
    def aide():
        if 'user_id' in session:
            user_id = session['user_id']
            user = User.query.get(user_id)
            return render_template('html/aide.html', title='aide', user=user)
        else:
            flash('Veuillez vous connecter pour accéder à cette page.', 'error')
            return redirect(url_for('login'))

    @app.route('/parametre')
    def parametre():
        if 'user_id' in session:
            user_id = session['user_id']
            user = User.query.get(user_id)
            return render_template('html/parametre.html', title='parametre', user=user)
        else:
            flash('Veuillez vous connecter pour accéder à cette page.', 'error')
            return redirect(url_for('login'))

    # Ajouter une catégorie
    @app.route('/categories', methods=['GET', 'POST'])
    def categories():
        form = CategoryForm()
        if form.validate_on_submit():
            category_name = form.name.data
            new_category = Category(name=category_name, user_id=session['user_id'])
            db.session.add(new_category)
            db.session.commit()
            flash('Catégorie ajoutée avec succès!', 'success')
            return redirect(url_for('categorie'))
        
        return render_template('html/AjouterCategorie.html', form=form)

    @app.route('/edit_category/<int:category_id>', methods=['GET', 'POST'])
    def edit_category(category_id):
        category = Category.query.get_or_404(category_id)
        form = EditCategoryForm(obj=category)
        
        if form.validate_on_submit():
            category.name = form.name.data
            db.session.commit()
            flash('Catégorie mise à jour avec succès!', 'success')
            return redirect(url_for('categorie'))

        return render_template('html/ModifierCategorie.html', form=form, category=category)

    @app.route('/delete_category/<int:category_id>', methods=['GET', 'POST'])
    def delete_category(category_id):
        category = Category.query.get_or_404(category_id)
        form = DeleteCategoryForm()

        if form.validate_on_submit():
            db.session.delete(category)
            db.session.commit()
            flash('Catégorie supprimée avec succès!', 'success')
            return redirect(url_for('categorie'))

        return render_template('html/SupprimeCategorie.html', form=form, category=category)

    # Ajouter une tâche
    @app.route('/add_task', methods=['GET', 'POST'])
    def add_task():
        form = TaskForm()

        # Charger les catégories depuis la base de données pour le champ 'category'
        form.category.choices = [(c.id, c.name) for c in Category.query.filter_by(user_id=session['user_id']).all()]

        if form.validate_on_submit():
            task = Task(
                title=form.title.data,
                description=form.description.data,
                start_date=form.start_date.data,
                end_date=form.end_date.data,
                category_id=form.category.data,
                user_id=session['user_id']
            )
            db.session.add(task)
            db.session.commit()
            flash('Tâche ajoutée avec succès!', 'success')
            return redirect(url_for('tache'))
        
        return render_template('html/Ajoutertache.html', form=form)
