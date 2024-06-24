"""
peça 5 numeros mostre quantos 9 r
"""
from time import sleep

print('  Informe 5 numeros')
p = float(input(' :'))
s = float(input(' :'))
t = float(input(' :'))
q = float(input(' :'))
qi = float(input(' :'))
# armazenamento
tupla = (p, s, t, q, qi)
nove = tupla.count(9)
print(f'  Aparições do nove(9): {nove}')
if tupla.count(3):
    sleep(1)
    tres = tupla.index(3) + 1
    print(f'  Posição do numero tres(3) :{tres}')
# armazem par
print('  Existem pares?')
for pos, i in enumerate(tupla):
    if i % 2 == 0:
        print(f'  O {pos+1}° numero - {i} é par')
# 08/05/2023 9:27Pm
