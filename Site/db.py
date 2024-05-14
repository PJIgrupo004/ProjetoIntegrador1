#Vou reunir tudo que necessitar de conexão ao banco em um arquivo só
from flask import current_app, g
import mysql.connector
import db_connection_data

#Verifica se já tem uma conexão no banco, caso contrário, cria uma nova
def getdb():
    if 'db' not in g or not g.db.is_connected():
        g.db = mysql.connector.connect(
            host=db_connection_data.host,
            user=db_connection_data.db_user,
            password=db_connection_data.db_password,
            database=db_connection_data.db_database
        )
    return g.db

#Função para fechar a conexão após cada solicitação para evitar múltiplas conexões
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None and db.is_connected():
        db.close()

def get_users():
    db = getdb()
    cursor = db.cursor(dictionary=True)
    cursor.execute('select usuario,id_usuario from usuarios')
    usuarios = cursor.fetchall()
    cursor.close()
    return usuarios

def get_password(user_name):
    db = getdb()
    cursor = db.cursor(dictionary=True)
    cursor.execute('select id_usuario,senha from usuarios where usuario ="'+user_name+'"')
    rt = cursor.fetchone()    
    print(rt)
    cursor.close()
    return rt

def get_id(id):
    db = getdb()
    cursor = db.cursor(dictionary=True)
    cursor.execute('select id_usuario from usuarios where id_usuario ='+id)
    id_ret = cursor.fetchone()
    cursor.close()
    return id_ret
