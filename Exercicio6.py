# Escreva um programa que abra um arquivo digitado pelo usuário e imprima seu conteúdo na tela.

nome_arquivo = input("Digite o nome do arquivo que deseja abrir: ")

try:
    # Tenta abrir o arquivo no modo de leitura
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        print("\nConteúdo do arquivo:")
        print(conteudo)
except FileNotFoundError:
    print("Arquivo não encontrado. Verifique o nome e tente novamente.")
except Exception as e:
    print(f"Ocorreu um erro ao abrir o arquivo: {e}")
