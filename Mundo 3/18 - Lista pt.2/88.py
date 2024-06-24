# pylint:disable=W0611
"""
crie x palpites da mega sena com seis numeros que não se repetem
"""
palpite = list()
from random import sample
from time import sleep

n = int(input('  Quantos palpites? '))
for i in range(n):
    palpite.append(sample(range(1, 61), 6))
for i, x in enumerate(palpite):
    print(f'Jogo {i+1}: {x}')
# 11/05/2023 10:49Pm
