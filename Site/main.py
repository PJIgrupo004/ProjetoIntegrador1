from flask import Flask, render_template
import requests

app = Flask(__name__)

#Tela inicial
@app.route("/")
def homepage():
    return render_template("home.html")

#Tela de login
@app.route("/login")
def login():
    return render_template("login.html")

#Tela de agendamento
@app.route("/agendamento")
def agendamento():
    return render_template("agendamento.html")

app.run()