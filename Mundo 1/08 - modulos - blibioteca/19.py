"""
sorteio de quatro alunos
"""
from random import choice

lista = []
n = 1
while n < 5:
    x = input(f'  Nome do aluno {n}: ')
    lista.append(x)
    n += 1
print(f'  Aluno sorteado: {choice(lista)}')
# 01/04/2023 5:26Pm
