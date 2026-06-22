from database.banco import conectar

def cadastrar_candidato():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        numero = int(input("\nNumero do candidato: "))
        nome = input("Nome do candidato: ").strip()
        partido = input("Partido: ").strip()

        if not nome or not partido:
            print("\nNome e partido não podem ser vazios.")
            return

        cursor.execute(""" 
        INSERT INTO candidatos (numero, nome, partido)
        VALUES (?, ?, ?)""", (numero, nome, partido))

        conexao.commit()

        print("\nCandidato cadastrado com sucesso!!!")
        
    except ValueError:
        print("\nNúmero inválido, digite apenas números.")
    except Exception as e:
        print(f"\nErro ao cadastrar candidato: {e}")
    finally:
        conexao.close()

def listar_candidatos():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""SELECT * FROM candidatos""")
        candidatos = cursor.fetchall()

        print("\n===== LISTA DE CANDIDATOS =====")
        if not candidatos:
            print("\nNenhum candidato cadastrado.")
        else:
            for id, numero, nome, partido in candidatos:
                print(f"ID: {id} - Nº: {numero} - Nome: {nome} - Partido: {partido}")

    except Exception as e:
        print(f"\nErro ao listar candidatos: {e}")
    finally:
        conexao.close()

def atualizar_candidato():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        id_candidato = int(input("\nDigite o ID do candidato para [atualizar]: "))
        nome_alterado = input("\nDigite o novo nome: ").strip()
        partido_alterado = input("Digite o novo partido: ").strip()

        if not nome_alterado or not partido_alterado:
            print("\nNome e partido não podem ser vazios.")
            return
        
        cursor.execute("""
        UPDATE candidatos SET nome = ?, partido = ?
        WHERE id = ?""", (nome_alterado, partido_alterado, id_candidato))

        if cursor.rowcount == 0:
            print("\nNenhum candidato encontrado com o ID informado.")
        else:
            conexao.commit()
            print("\nCandidato alterado com sucesso!!!")

    except ValueError:
        print("\nID inválido, digite apenas números.")
    except Exception as e:
        print(f"\nErro ao atualizar candidato: {e}")
    finally:
        conexao.close()

def excluir_candidato():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        id_candidato = int(input("\nDigite o ID do candidato para [excluir]: "))

        cursor.execute("""
        DELETE FROM candidatos
        WHERE id = ? """, (id_candidato,))

        if cursor.rowcount == 0:
            print("\nNenhum candidato encontrado com o ID informado.")
        else:
            conexao.commit()
            print("\nCandidato excluido com sucesso!!!")
    except ValueError:
        print("\nID inválido, digite apenas números.")
    except Exception as e:
        print(f"\nErro ao excluir candidato: {e}")
    finally:
        conexao.close()

def buscar_candidato(numero):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT * FROM candidatos
        WHERE numero = ? """, (numero,))

        candidato = cursor.fetchone()

    except Exception as e:
        print(f"\nErro ao buscar candidato: {e}")
    finally:
         conexao.close()
    
    return candidato
