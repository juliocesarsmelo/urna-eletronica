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
        numero INTEGER UNIQUE NOT NULL,
        nome TEXT NOT NULL,
        partido TEXT NOT NULL
    )
    """)

    #Eleitores
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS eleitores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cpf TEXT UNIQUE NOT NULL,
        nome TEXT NOT NULL,
        votou INTEGER DEFAULT 0
    )
    """)

    #Votos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS votos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        eleitor_id INTEGER NOT NULL,
        candidato_id INTEGER NOT NULL,
        FOREIGN KEY(eleitor_id) REFERENCES eleitores(id),
        FOREIGN KEY(candidato_id) REFERENCES candidatos(id)
    )
    """)

    conexao.commit()
    conexao.close()