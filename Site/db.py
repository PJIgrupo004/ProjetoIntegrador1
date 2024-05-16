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

class cliente():
    #Retorna todos os clientes
    def get_clientes():
        db = getdb()
        cursor = db.cursor(dictionary=True)
        cursor.execute('select * from clientes')
        clientes = cursor.fetchall()    
        print(clientes)
        cursor.close()
        return clientes
    
    #Insere um cliente novo na tabela
    def insert_cliente(nome,telefone,data_nascimento,endereco,facebook,instagram):
        db = getdb()
        cursor = db.cursor(dictionary=True)
        cursor.execute('insert into clientes (nome,telefone,data_nascimento,endereco,facebook,instagram) values ('+nome+','+telefone+','+data_nascimento+','+endereco+','+facebook+','+instagram+')')
        db.commit()  
        cursor.close()
        return cursor.lastrowid()
    
    def update_cliente(nome,telefone,data_nascimento,endereco,facebook,instagram):
        db = getdb()
        cursor = db.cursor(dictionary=True)
        cursor.execute('update clientes set (nome,telefone,data_nascimento,endereco,facebook,instagram) values ('+nome+','+telefone+','+data_nascimento+','+endereco+','+facebook+','+instagram+')')
        db.commit()  
        affected_rows = cursor.rowcount
        if affected_rows is not None and affected_rows > 0:
            cursor.close()
            return True
        else:
            return False
        

class procedimentos():
    
    #Retorna todos os procedimentos
    def get_procedimentos():
        db = getdb()
        cursor = db.cursor(dictionary=True)
        cursor.execute('select * from procedimentos')
        procedimentos = cursor.fetchall()    
        print(procedimentos)
        cursor.close()
        return procedimentos
    
    #Insere um novo procedimento
    def insert_procedimento(nome,tempo,valor,descricao):
        db = getdb()
        cursor = db.cursor(dictionary=True)
        cursor.execute('insert into procedimentos (nome,tempo,valor,descricao) values ('+nome+','+tempo+','+valor+','+descricao+')')
        db.commit()  
        cursor.close()
        return cursor.lastrowid()
    
    def update_procedimento(nome,tempo,valor,descricao):
        db = getdb()
        cursor = db.cursor(dictionary=True)
        cursor.execute('update procedimentos set (nome,tempo,valor,descricao) values ('+nome+','+tempo+','+valor+','+descricao+')')
        db.commit()  
        cursor.close()
        affected_rows = cursor.rowcount
        if affected_rows is not None and affected_rows > 0:
            cursor.close()
            return True
        else:
            return False

class produtos():
    
    #Retorna todos os produtos
    def get_produtos():
        db = getdb()
        cursor = db.cursor(dictionary=True)
        cursor.execute('select * from produtos')
        produtos = cursor.fetchall()    
        print(produtos)
        cursor.close()
        return produtos
    
    #Insere um novo produto
    def insert_produto(nome,marca,valor,data_validade,quant_estoque):
        db = getdb()
        cursor = db.cursor(dictionary=True)
        cursor.execute('insert into produtos (nome,marca,valor,data_validade,quant_estoque) values ('+nome+','+marca+','+valor+','+data_validade+','+quant_estoque+')')
        db.commit()  
        cursor.close()
        return cursor.lastrowid()  

    def update_produto(nome,marca,valor,data_validade,quant_estoque):
        db = getdb()
        cursor = db.cursor(dictionary=True)
        cursor.execute('update produtos set (nome,marca,valor,data_validade,quant_estoque) values ('+nome+','+marca+','+valor+','+data_validade+','+quant_estoque+')')
        db.commit()  
        cursor.close()
        affected_rows = cursor.rowcount
        if affected_rows is not None and affected_rows > 0:
            cursor.close()
            return True
        else:
            return False
    
class agendamentos():

    def get_agendamentos():
        db = getdb()
        cursor = db.cursor(dictionary=True)
        cursor.execute('select * from agendamentos')
        agendamentos = cursor.fetchall()    
        print(agendamentos)
        cursor.close()
        return agendamentos
    
    def insert_agendamentos(id_cliente,id_procedimento,data_agendamento,hora_agendamento,data_realização,status,observacoes):
        db = getdb()
        cursor = db.cursor(dictionary=True)
        cursor.execute('insert into agendamentos (id_cliente,id_procedimento,data_agendamento,hora_agendamento,data_realização,status,observacoes) values ('+id_cliente+','+id_procedimento+','+data_agendamento+','+hora_agendamento+','+data_realização+','+status+','+observacoes+')')
        db.commit()
        cursor.close()
        return cursor.lastrowid()
    
    def update_agendamentos(id_cliente,id_procedimento,data_agendamento,hora_agendamento,data_realização,status,observacoes):
        db = getdb()
        cursor = db.cursor(dictionary=True)
        cursor.execute('update agendamentos set (id_cliente,id_procedimento,data_agendamento,hora_agendamento,data_realização,status,observacoes) values ('+id_cliente+','+id_procedimento+','+data_agendamento+','+hora_agendamento+','+data_realização+','+status+','+observacoes+')')
        db.commit()
        cursor.close()
        affected_rows = cursor.rowcount
        if affected_rows is not None and affected_rows > 0:
            cursor.close()
            return True
        else:
            return False