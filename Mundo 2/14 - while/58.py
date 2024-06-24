"""
faça o programa pensar em um numero entre 0 e 10 e faça o usuario adivinhar até acerta depois imprima a quantidade de chutes
"""
amarelo = '\033[1;33m'
cont = 1
limpar = '\033[0;0m'
estilo = f'{amarelo}  Chute {cont}{limpar}'
from random import randint

bot = randint(1, 10)
user = int(input('  Adivinhe : '))
while user != bot:
    cont += 1
    print(estilo)
    user = int(input('  Adivinhe : '))

print(f'  Chutes até acerta {cont-1}')
