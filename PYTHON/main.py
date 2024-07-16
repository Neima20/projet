from flask import Flask, render_template, request, session, redirect ,url_for, flash, session

from Model import db , User

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Ecole.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'


db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
@app.route('/index')
def index():
    return render_template('PageConnexion.html', name="ali", title="Acceuil")








@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=="POST":
        email=request.form['email']
        password=request.form['password']
        
        # Récupérer l'utilisateur correspondant à l'email fourni
        user = User.query.filter_by(email=email).first()
        if user:
            # Vérifier si le mot de passe correspond
            if user.password== password:
                flash('Vous êtes connecté!', 'success')
                 # Stocker l'ID de l'utilisateur dans la session
                session['user_id'] = user.id
                return redirect(url_for('index'))
            else:
                flash('Mot de passe incorrect!', 'error')
        else:
           
            flash('Utilisateur non trouvé!', 'error')       
    return render_template('login.html', title='Login')
    
    




    # @app.route('/')
# @app.route('/html')
# def html():
#     return 'PageConnexion.html'
                           
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method=="POST":
#         email=request.form['email']
#         password=request.form['password']
        
#         # Récupérer l'utilisateur correspondant à l'email fourni
#         user = User.query.filter_by(email=email).first()
#         if user:
#             # Vérifier si le mot de passe correspond
#             if user.password== password:
#                 flash('Vous êtes connecté!', 'success')
#                  # Stocker l'ID de l'utilisateur dans la session
#                 session['user_id'] = user.id
#                 return redirect(url_for('index'))
#             else:
#                 flash('Mot de passe incorrect!', 'error')
#         else:
           
#             flash('Utilisateur non trouvé!', 'error')       
#     return render_template('login.html', title='Login')
   


# @app.route('/inscription', methods=['GET', 'POST'])
# def inscription():
#     if request.method=='POST':
#         nom=request.form['usename']
#         email=request.form['email']
#         Numero=request.form['tel']
#         password=request.form['password']
#         RePassword=request.form['RePassword']
#         if password != RePassword:
#             flash('le deux mot de passe ne sont pas le meme', 'error')
#             return redirect(url_for('inscription'))
#         else:
            
#             newUser=User(nom=nom, email=email, numero=Numero, password=password)
#             db.session.add(newUser)
#             db.session.commit()
#             flash("Brovo! vous etes bien Inscrit", "success")
#             return redirect(url_for('login'))
#     return render_template('inscription.html', title='inscription')

# @app.route('/sedeconnecter')
# def deconnecter():
    
#     # Supprimer l'ID de l'utilisateur de la session
#     session.pop('user_id', None)
#     flash('Vous êtes déconnecté!', 'success')
#     return redirect(url_for('login'))

# @app.route('/formation')
# def formation():
#     return render_template('formation.html', title="formation")



# @app.route('/contact')
# def contact():
#     return render_template('contact.html', title='contact')
# if __name__=="__main__":
#     app.run(debug=True)


