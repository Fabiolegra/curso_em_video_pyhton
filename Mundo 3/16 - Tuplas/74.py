"""
aramzene 5 numeros aleatorios em uma tupla.
depois mostre os numeros e o maior e o menor
"""
from random import randint

style = '==' * 20
style2 = '--' * 20
text = '  NUMEROS ALEATÓRIOS'
sort = '  SORTEADOS'
print('{}\n{}\n{}'.format(style, text, style))
# variaveis
p = randint(0, 10)
t = randint(0, 10)
q = randint(0, 10)
qi = randint(0, 10)
s = randint(0, 10)
# armazenamento
tupla = (p, s, t, q, qi, s)
# colocando em ordem
x = sorted(tupla)
menor = x[0]
maior = x[-1]
print('{}: {}'.format(sort, tupla))
print(f'  MAIOR: {maior}\n  MENOR: {menor}')
# 08/05/2023 7:36Pm
