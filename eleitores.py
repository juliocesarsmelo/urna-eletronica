from database.banco import conectar

def cadastrar_eleitor():
    conexao = conectar()
    cursor = conexao.cursor()

    print("\nCadastrar Eleitor")
    cpf = input("CPF: ")
    nome = input("Nome: ")

    try:
        cursor.execute("""
        INSERT INTO eleitores (cpf, nome)
        VALUES (?, ?) """, 
        (cpf, nome))

        conexao.commit()

        print("\nEleitor cadastrado com sucesso!!!")

    except:
        print("\nERRO ao cadastrar eleitor, por favor tente novamente.")
        #Refatorar, com um try cath

    conexao.close()

def buscar_eleitor_por_cpf(cpf):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM eleitores
    WHERE cpf = ? """, (cpf,))

    eleitor = cursor.fetchone()

    conexao.close()

    if eleitor is None:
        return print("Eleitor não encontrado!!!")
        #necessário refatorar
    
    if eleitor[3] == 1:
        return print("Eleitor já votou!!!")
        #necessário refatorar
    print(eleitor)
    return eleitor

def atualizar_status_voto_eleitor(id_eleitor):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE eleitores
    SET votou = 1
    WHERE id = ? """, 
    (id_eleitor,))

    conexao.commit()
    conexao.close()




