-- Criação da tabela de candidatos
CREATE TABLE IF NOT EXISTS candidatos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero INTEGER UNIQUE NOT NULL,
    nome TEXT NOT NULL,
    partido TEXT NOT NULL
);

-- Criação da tabela de eleitores
CREATE TABLE IF NOT EXISTS eleitores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cpf TEXT UNIQUE NOT NULL,
    nome TEXT NOT NULL,
    votou INTEGER DEFAULT 0
);

-- Criação da tabela de votos
CREATE TABLE IF NOT EXISTS votos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    eleitor_id INTEGER NOT NULL,
    candidato_id INTEGER NOT NULL,
    FOREIGN KEY(eleitor_id) REFERENCES eleitores(id),
    FOREIGN KEY(candidato_id) REFERENCES candidatos(id)
);