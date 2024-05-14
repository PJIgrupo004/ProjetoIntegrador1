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

#Traz o ID de todos os usuários
def get_users():
    db = getdb()
    cursor = db.cursor(dictionary=True)
    cursor.execute('select id_usuario from usuarios')
    usuarios = cursor.fetchall()
    cursor.close()
    return usuarios

#Retorna o ID e a senha a partir do nome do usuário
def get_password_user(user_name):
    db = getdb()
    cursor = db.cursor(dictionary=True)
    print('select id_usuario,senha from usuarios where usuario ="'+user_name+'"')
    cursor.execute('select id_usuario,senha from usuarios where usuario ="'+user_name+'"')
    rt = cursor.fetchone()    
    cursor.close()
    return rt

#Retorna o ID e a senha a partir do ID
def get_password_id(id):
    db = getdb()
    cursor = db.cursor(dictionary=True)
    print('select id_usuario,senha from usuarios where id_usuario ='+id)
    cursor.execute('select id_usuario,senha from usuarios where id_usuario ='+id)
    rt = cursor.fetchone()    
    cursor.close()
    return rt

#Retorna a listagem dos posts do instagram
def get_posts():
    db = getdb()
    cursor = db.cursor(dictionary=True)
    cursor.execute('select embedded from posts_instagram '
                   +'where (Data_inicial_exibicao <= now() or Data_inicial_exibicao is null) '
                   +'and (Data_final_exibicao >= now() or Data_final_exibicao is null) '
                   +'and status = "A"')
    rt = cursor.fetchall()    
    cursor.close()
    return rt
