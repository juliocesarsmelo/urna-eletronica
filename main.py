from database.banco import criar_tabelas
from candidatos import *
from eleitores import *
from votos import votar

criar_tabelas()

for i in range(5):
    cadastrar_candidato()

listar_candidatos()

atualizar_candidato()

excluir_candidato()

listar_candidatos()

cadastrar_eleitor()

votar()