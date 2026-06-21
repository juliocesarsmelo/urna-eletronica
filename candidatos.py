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
    