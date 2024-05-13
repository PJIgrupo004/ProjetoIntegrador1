from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_required, current_user, login_user, logout_user
import requests


app = Flask(__name__)
app.secret_key = 'chave'
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, username, password):
        self.id = username
        self.password = password

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

#Consultar BD, mas usar mockado por hora
users = {'user': User('user', '1234')}

#Tela inicial
@app.route("/")
def homepage():
    return render_template("jinja_home.html")

#Tela de agendamento
@app.route("/agendamento")
def agendamento():
    return render_template("jinja_agendamento.html")

#Tela principal do administrador
@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("/adm/jinja_dashboard.html")

#Tela de login
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
         return redirect(url_for('dashboard'))
    else:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            # Aqui deve ter a requisição de autenticação do backend
            user = users.get(username)
            if user and user.password == password:
                login_user(user)
                return redirect(url_for('dashboard'))
        return render_template('jinja_login.html')

# Rota de logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))

if __name__ == '__main__':
    app.run()

