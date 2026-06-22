from database.banco import criar_tabelas
from candidatos import cadastrar_candidato, listar_candidatos, atualizar_candidato, excluir_candidato
from eleitores import cadastrar_eleitor, listar_eleitores, atualizar_eleitor, excluir_eleitor
from votos import votar, apurar_votos

def menu():
    criar_tabelas()

    while True:
        print("\n===== URNA ELETRÔNICA =====")
        print("1 - Cadastrar candidato")
        print("2 - Listar candidatos")
        print("3 - Atualizar candidato")
        print("4 - Excluir candidato")
        print("5 - Cadastrar eleitor")
        print("6 - Listar eleitores")
        print("7 - Atualizar eleitor")
        print("8 - Excluir eleitor")
        print("9 - Votar")
        print("10 - Apurar votos")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_candidato()
        elif opcao == "2":
            listar_candidatos()
        elif opcao == "3":
            atualizar_candidato()
        elif opcao == "4":
            excluir_candidato()
        elif opcao == "5":
            cadastrar_eleitor()
        elif opcao == "6":
            listar_eleitores()
        elif opcao == "7":
            atualizar_eleitor()
        elif opcao == "8":
            excluir_eleitor()
        elif opcao == "9":
            votar()
        elif opcao == "10":
            apurar_votos()
        elif opcao == "0":
            print("\nEncerrando sistema... Até logo!")
            break
        else:
            print("\nOpção inválida, tente novamente.")

if __name__ == "__main__":
    menu()



