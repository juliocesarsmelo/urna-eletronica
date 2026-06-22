from database.banco import conectar

def cadastrar_candidato():
    conexao = conectar()
    cursor = conexao.cursor()

    numero = int(input("\nNumero do candidato: "))
    nome = input("Nome do candidato: ")
    partido = input("Partido: ")

    try:
        cursor.execute(""" 
        INSERT INTO candidatos (numero, nome, partido)
        VALUES (?, ?, ?)""", 
        (numero, nome, partido))

        conexao.commit()
        print("\nCandidato cadastrado com sucesso!!!")
        
    except:
        print("\nERRO!!! número já cadastrado, por favor tente novamente.")

    conexao.close()

def listar_candidatos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""SELECT * FROM candidatos""")

    print("\n===== LISTA DE CANDIDATOS =====")

    for id, numero, nome, partido in cursor.fetchall():
        print(f"ID: {id} - Nº: {numero} - Nome: {nome} - Partido: {partido}")

    conexao.close()

def atualizar_candidato():
    conexao = conectar()
    cursor = conexao.cursor()

    id_candidato = int(input("\nDigite o ID do candidato para [atualizar]: "))

    nome_alterado = input("\nDigite o novo nome: ")
    partido_alterado = input("Digite o novo partido: ")

    cursor.execute("""
    UPDATE candidatos       
    SET nome = ?, partido = ?
    WHERE id = ?""", 
    (nome_alterado, partido_alterado, id_candidato))

    conexao.commit()
    conexao.close()

    print("\nCandidato alterado com sucesso!!!")

def excluir_candidato():
    conexao = conectar()
    cursor = conexao.cursor()

    id_candidato = int(input("\nDigite o ID do candidato para [excluir]: "))

    cursor.execute("""
    DELETE FROM candidatos
    WHERE id = ? """, 
    (id_candidato,))

    conexao.commit()
    conexao.close()

    print("\nCandidato excluido com sucesso!!!")
    
