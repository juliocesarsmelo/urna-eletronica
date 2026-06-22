from database.banco import conectar

def cadastrar_candidato():
    conexao = conectar()
    cursor = conexao.cursor()

    numero = int(input("Numero do candidato: "))
    nome = input("Nome do candidato: ")
    partido = input("Partido: ")

    try:
        cursor.execute(""" 
        INSERT INTO candidatos (numero, nome, partido)
        VALUES (?, ?, ?)""", 
        (numero, nome, partido))

        conexao.commit()
        print("Candidato cadastrado com sucesso!")
        
    except:
        print("ERRO!!! número já cadastrado, por favor tente novamente.")

    conexao.close()

def listar_candidatos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""SELECT * FROM candidatos""")

    print("\n===== LISTA DE CANDIDATOS =====")

    for _, numero, nome, partido in cursor.fetchall():
        print(f"Nº: {numero} - Nome: {nome} - Partido: {partido}")

    print("\n")

    conexao.close()