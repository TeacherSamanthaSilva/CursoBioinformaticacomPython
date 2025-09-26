# Escreva um programa que exiba um menu e pergunte o que o usuário deseja fazer. Se o usuário digitar 1, o programa deve chamar uma função que lê um arquivo de texto. Se o usuário apertar 2, o programa deve imprimir o conteúdo do arquivo lido anteriormente. Se o usuário apertar três o programa deve ser fechado.

# Função para ler o conteúdo de um arquivo
def ler_arquivo():
    nome_arquivo = input("Digite o nome do arquivo que deseja ler: ")
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print("Arquivo lido com sucesso.")
            return conteudo
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None

# Função principal com menu
def menu():
    conteudo_arquivo = None
    while True:
        print("\nMenu:")
        print("1 - Ler um arquivo de texto")
        print("2 - Mostrar conteúdo do arquivo lido")
        print("3 - Sair")

        escolha = input("Digite sua opção: ")

        if escolha == '1':
            conteudo_arquivo = ler_arquivo()
        elif escolha == '2':
            if conteudo_arquivo:
                print("\nConteúdo do arquivo:")
                print(conteudo_arquivo)
            else:
                print("Nenhum arquivo foi lido ainda.")
        elif escolha == '3':
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu
menu()
