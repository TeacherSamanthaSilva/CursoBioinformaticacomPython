# Escreva um programa que leia um arquivo multi-fasta e armazene em um dicionário: cabeçalho da sequência como a chave e a sequência como valor.

def ler_multi_fasta(nome_arquivo):
    sequencias = {}
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            cabecalho = None
            sequencia = ''
            for linha in arquivo:
                linha = linha.strip()
                if linha.startswith('>'):
                    if cabecalho:
                        sequencias[cabecalho] = sequencia
                    cabecalho = linha[1:]  # Remove o '>'
                    sequencia = ''
                else:
                    sequencia += linha
            if cabecalho:
                sequencias[cabecalho] = sequencia
        return sequencias
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return {}
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return {}

# Exemplo de uso
nome_arquivo = input("Digite o nome do arquivo multi-FASTA: ")
resultado = ler_multi_fasta(nome_arquivo)

# Exibe o dicionário
for cabecalho, sequencia in resultado.items():
    print(f"\n>{cabecalho}\n{sequencia}")
