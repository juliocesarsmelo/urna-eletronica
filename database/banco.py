import sqlite3

def conectar():
    conexao = sqlite3.connect("urna.db")
    return conexao

def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    #Candidatos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS candidatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero INTEGER UNIQUE,
        nome TEXT NOT NULL,
        partido TEXT NOT NULL
    )
    """)

    #Eleitores
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS eleitores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cpf TEXT UNIQUE,
        nome TEXT NOT NULL,
        votou INTEGER DEFAULT 0
    )
    """)

    #Votos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS votos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        eleitor_id INTEGER,
        candidato_id INTEGER
    )
    """)

    conexao.commit()
    conexao.close()