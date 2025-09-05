#Escreva um programa que ordene uma lista numérica com três elementos.

# Entrada
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

# Ordenação manual
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

print("Números em ordem crescente:", a, b, c)
