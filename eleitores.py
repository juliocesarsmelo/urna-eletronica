from database.banco import conectar

def cadastrar_eleitor():
    conexao = conectar()
    cursor = conexao.cursor()

    cpf = input("CPF: ")
    nome = input("Nome: ")

    try:
        cursor.execute("""
        INSERT INTO eleitores (cpf, nome)
        VALUES (?, ?) """, 
        (cpf, nome))

        print("\nEleitor cadastrado com sucesso!!!")

    except:
        print("\nERRO ao cadastrar eleitor, por favor tente novamente.")

    conexao.close()




