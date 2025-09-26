#Escreva um programa que receba uma sequência digitada pelo usuário e a salve num arquivo no formato fasta.

# Solicita a sequência ao usuário
sequencia = input("Digite a sequência (ex: ATCGGCTA): ")

# Solicita um identificador para a sequência
identificador = input("Digite um identificador para a sequência (ex: seq1): ")

# Define o nome do arquivo de saída
nome_arquivo = identificador + ".fasta"

try:
    # Abre o arquivo para escrita e salva no formato FASTA
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(f">{identificador}\n")
        arquivo.write(sequencia + "\n")
    print(f"Sequência salva com sucesso em '{nome_arquivo}' no formato FASTA.")
except Exception as e:
    print(f"Ocorreu um erro ao salvar o arquivo: {e}")
