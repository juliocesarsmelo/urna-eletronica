from database.banco import conectar

def cadastrar_eleitor():
    conexao = conectar()
    cursor = conexao.cursor()

    try:

        print("\n===== CADASTRAR ELEITOR =====")
        cpf = input("CPF: ").strip(".,:/-)(")
        nome = input("Nome: ").strip()

        if not cpf or not nome:
            print("\nCPF e Nome não podem ser vazios.")
            return

        if not cpf.isdigit() or len(cpf) != 11:
            print("CPF inválido, digite apenas números com 11 dígitos.")
            return
        
        cursor.execute("""
        INSERT INTO eleitores (cpf, nome)
        VALUES (?, ?) """, (cpf, nome))

        conexao.commit()

        print("\nEleitor cadastrado com sucesso!!!")

    except Exception as e:
        print(f"\nERRO ao cadastrar eleitor: {e}")
    finally:
        conexao.close()

def listar_eleitores():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""SELECT * FROM candidatos""")
        eleitores = cursor.fetchall()

        print("\n===== LISTA DE ELEITORES =====")

        if not eleitores:
            print("\nNenhum eleitor cadastrado.")
        else:
            for id, cpf, nome, votou in eleitores:
                status = "Já votou" if votou == 1 else "Não votou"
                print(f"ID: {id} - CPF: {cpf} - Nome: {nome} - Status: {status}")
    except Exception as e:
        print(f"\nErro ao listar eleitores: {e}")
    finally:
        conexao.close()

def buscar_eleitor_por_cpf(cpf):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT * FROM eleitores
        WHERE cpf = ? """, (cpf,))

        eleitor = cursor.fetchone()
    
    except Exception as e:
        print(f"/nErro ao buscar eleitor: {e}")
        eleitor = None
    finally:
         conexao.close()

    return eleitor

def atualizar_eleitor():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        id_eleitor = int(input("\nDigite o ID do eleitor para [atualizar]: "))        
        cpf_alterado = input("Digite o novo CPF: ").strip(".,:/-)(")
        nome_alterado = input("Digite o novo nome: ").strip()

        if not cpf_alterado or not nome_alterado:
            print("\nCPF e Nome não podem ser vazios.")
            return
        
        if not cpf_alterado.isdigit() or len(cpf_alterado) != 11:
            print("CPF inválido, digite apenas números com 11 dígitos.")
            return
        
        cursor.execute("""
        UPDATE eleitores SET nome = ?, cpf = ? 
        WHERE id = ? """, (nome_alterado, cpf_alterado, id_eleitor))

        if cursor.rowcount == 0:
            print("\nNenhum eleitor encontrado com esse ID.")
        else:
            conexao.commit()
            print("\nEleitor atualizado com sucesso!!!")
    except ValueError:
        print("\nID inválido, digite apenas números.")
    except Exception as e:
        print(f"\nErro ao atualizar eleitor: {e}")
    finally:
        conexao.close()

def atualizar_status_voto_eleitor(id_eleitor):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        UPDATE eleitores SET votou = 1
        WHERE id = ? """, (id_eleitor,))

        conexao.commit()

    except Exception as e:
        print(f"\nErro ao atualizar status de voto: {e}")
    finally:
        conexao.close()

def excluir_eleitor():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        id_eleitor = int(input("\nDigite o ID do eleitor para [excluir]: "))

        cursor.execute("""
        DELETE FROM eleitores 
        WHERE id = ? """, (id_eleitor,))

        if cursor.rowcount == 0:
            print("\nNenhum eleitor encontrado com esse ID.")
        else:
            conexao.commit()
            print("\nEleitor excluído com sucesso!!!")

    except ValueError:
        print("\nID inválido, digite apenas números.")
    except Exception as e:
        print(f"\nErro ao excluir eleitor: {e}")
    finally:
        conexao.close()

