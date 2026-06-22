from database.banco import conectar
from eleitores import buscar_eleitor_por_cpf, atualizar_status_voto_eleitor
from candidatos import listar_candidatos, buscar_candidato

def votar():
    conexao = conectar()
    cursor = conexao.cursor()

    cpf = input("Digite o CPF do eleitor: ")

    eleitor = buscar_eleitor_por_cpf(cpf) #necessário refatorar

    listar_candidatos()

    numero = int(input("Digite o número do candidato: "))

    candidato = buscar_candidato(numero) #necessário refatorar

    cursor.execute("""
    INSERT INTO votos (eleitor_id, candidato_id)
    VALUES (?, ?)
    """, (eleitor[0], candidato[0]))

    conexao.commit()
    conexao.close()

    atualizar_status_voto_eleitor(eleitor[0])

    print("Voto realizado com sucesso!!!")

    
    
