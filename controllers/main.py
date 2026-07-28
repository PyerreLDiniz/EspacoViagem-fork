from fasthtml.common import *
import sys
import os

# Pequeno truque para o Python achar a nossa pasta 'views'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from views.home import layout_admin, layout_cadastro, layout_login, layout_pagina_inicial, layout_tabela_usuarios
from models.auth import authenticate_user, create_user, delete_user_by_id, get_all_users, init_db
import sqlite3

# Inicializamos o aplicativo FastHTML
app, rt = fast_app()

init_db()

# Tela de login inicial
@rt('/')
def login():
    return Title("Login - Espaço Viagem"), layout_login()

# Página principal após o login
@rt('/home')
def home(username: str = None, password: str = None):
    if username and password and authenticate_user(username, password):
        if username.strip().lower() == "admin":
            return Title("Painel admin"), layout_admin(get_all_users())
        return Title("Espaço Viagem"), layout_pagina_inicial()
    return Title("Login - Espaço Viagem"), layout_login("Usuário ou senha inválidos")

@rt('/admin/create')
def admin_create(username: str = None, password: str = None):
    if username and password and authenticate_user("admin", "admin123"):
        if create_user(username, password):
            return Title("Admin"), layout_admin(get_all_users(), success_message="Usuário criado com sucesso.")
        return Title("Admin"), layout_admin(get_all_users(), error_message="Não foi possível criar. Verifique o nome.")
    return Title("Login - Espaço Viagem"), layout_login("Acesso restrito ao admin")

@rt('/admin/delete/{user_id:int}')
def admin_delete(user_id: int):
    if authenticate_user("admin", "admin123"):
        if delete_user_by_id(user_id):
            return Title("Admin"), layout_admin(get_all_users(), success_message="Usuário removido com sucesso.")
        return Title("Admin"), layout_admin(get_all_users(), error_message="Não foi possível remover esse usuário.")
    return Title("Login - Espaço Viagem"), layout_login("Acesso restrito ao admin")

@rt('/cadastrar')
def cadastrar(username: str = None, password: str = None):
    if username and password:
        if create_user(username, password):
            return Title("Cadastro concluído"), layout_cadastro(success_message="Conta criada com sucesso! Agora você pode entrar.")
        return Title("Cadastro"), layout_cadastro(error_message="Não foi possível criar a conta. Esse usuário já existe.")
    return Title("Cadastro"), layout_cadastro()

@rt('/usuarios')
def usuarios():
    conn = sqlite3.connect("espaco_viagem.db")
    rows = conn.execute("SELECT id, username FROM users ORDER BY id").fetchall()
    conn.close()
    usuarios = [{"id": row[0], "username": row[1]} for row in rows]
    return Title("Usuários cadastrados"), layout_tabela_usuarios(usuarios)

# Ligamos o servidor!
serve()