""" Escreva um programa que resolva uma equação de segundo grau. """

import math

# Entrada de dados
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Calcula o discriminante (delta)
delta = b**2 - 4*a*c

if a == 0:
    print("Não é uma equação do segundo grau.")
else:
    if delta < 0:
        print("Não existem raízes reais.")
    elif delta == 0:
        x = -b / (2*a)
        print(f"A equação tem uma raiz real: x = {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"As raízes da equação são: x1 = {x1} e x2 = {x2}")
