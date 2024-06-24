"""
sorteio de quatro alunos e as ordems de apresentação
"""
import random

alunos = []
n = 1
for x in range(1, 5):
    x = input(f'  Nome do aluno {n}:   : ')
    alunos.append(x)
    n += 1
for i in range(1, 5):
    print(f'  {i} Aluno sorteado {alunos.pop()}')
# 01/05/2023 5:34Pm
