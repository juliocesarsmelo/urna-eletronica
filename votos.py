from database.banco import conectar
from eleitores import buscar_eleitor_por_cpf, atualizar_status_voto_eleitor
from candidatos import listar_candidatos, buscar_candidato

def votar():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        print("\n===== VOTAÇÃO =====")
        cpf = input("Digite o CPF do eleitor: ").strip(".,:/-)(")

        if not cpf.isdigit() or len(cpf) != 11:
            print("CPF inválido, digite apenas números com 11 dígitos.")
            return
        
        eleitor = buscar_eleitor_por_cpf(cpf) 

        if not eleitor:
            print("\nEleitor não encontrado")
            return
        
        if eleitor[3] == 1:
            print("\nEleitor já votou.")
            return
        
        listar_candidatos()

        numero = int(input("Digite o número do candidato: "))

        candidato = buscar_candidato(numero)

        if not candidato:
            print("\nCandidato inválido.")
            return
        
        cursor.execute("""
        INSERT INTO votos (eleitor_id, candidato_id)
        VALUES (?, ?) """, (eleitor[0], candidato[0]))

        conexao.commit()

        atualizar_status_voto_eleitor(eleitor[0])

        print("\nVoto realizado com sucesso!!!")

    except ValueError:
        print("\nNúmero inválido, digite apenas números.")
    except Exception as e:
        print(f"\nErro ao registrar voto: {e}")
    finally:
        conexao.close()

def apurar_votos():
    conexao = conectar()
    cursor = conexao.cursor() 

    try:
        cursor.execute("""
        SELECT candidatos.nome, COUNT(votos.id) as total
        FROM candidatos
        LEFT JOIN votos ON candidatos.id = votos.candidato_id
        GROUP BY candidatos.id
        ORDER BY total DESC
        """)

        resultados = cursor.fetchall()

        print("\n===== RESULTADO FINAL =====")

        if not resultados:
            print("Nenhum voto registrado.")
        else:
            for nome, total in resultados:
                print(f"{nome}: {total} votos")
            print(f"\nVencedor: {resultados[0][0]}")
    except Exception as e:
        print(f"\nErro ao apurar resultados: {e}")
    finally:
        conexao.close()

    
    
