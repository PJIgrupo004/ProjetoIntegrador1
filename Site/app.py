from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_required, current_user, login_user, logout_user
import db


app = Flask(__name__)
app.secret_key = 'chave'
app.app_context().push()
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
db.getdb()

class User(UserMixin):

    def __init__(self, username, password):
        self.id = username
        self.password = password

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

@login_manager.user_loader
def load_user(user_id):
    usuario = db.get_password_user(user_id)
    return User(usuario['id_usuario'],usuario['senha'])


#Tela inicial
@app.route("/")
def homepage():
    return render_template("jinja_home.html",posts = db.get_posts())

#Tela de agendamento
@app.route("/agendamento")
def agendamento():
    return render_template("jinja_agendamento.html")

#Tela de login
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
         return redirect(url_for('dashboard'))
    else:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            ret = db.get_password_user(username)
            if ret != None:
                user = User(username,password)
                if user.password == password:
                    login_user(user)
                    return redirect(url_for('dashboard'))
        return render_template('jinja_login.html')

#Tela principal do administrador
@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("/adm/jinja_dashboard.html")

#Tela Cadastro de Clientes
@app.route("/cadastro_cliente")
@login_required
def cadastro_cliente():
    #Pra cadastrar um cliente, chame a função db.cliente.insert_cliente(nome,telefone,data_nascimento,endereco,facebook,instagram)
    #Precisa informar todos os campos (mesma que seja None/Null), então é bom inicializar as variáveis
    return render_template("/adm/jinja_cadastro_cliente.html")

#Tela Cadastro de Serviços
@app.route("/cadastro_serviços")
@login_required
def cadastro_servicos():
    return render_template("/adm/jinja_cadastro_serviços.html")

#Tela Cadastro de Funcionarios
@app.route("/cadastro_funcionarios")
@login_required
def cadastro_funcionarios():
    return render_template("/adm/jinja_cadastro_funcionarios.html")

#Tela Clientes Cadastrados
@app.route("/clientes_cadastrados")
@login_required
def clientes_cadastrados():
    return render_template("/adm/jinja_clientes_cadastrados.html",clientes=db.cliente.get_clientes())

#Tela Serviços Cadastrados
@app.route("/serviços_cadastrados")
@login_required
def servicos_cadastrados():
    return render_template("/adm/jinja_serviços_cadastrados.html")

#Tela Funcionarios Cadastrados
@app.route("/funcionarios_cadastrados")
@login_required
def funcionarios_cadastrados():
    return render_template("/adm/jinja_funcionarios_cadastrados.html")

# Rota de logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))

if __name__ == '__main__':
    app.run()

