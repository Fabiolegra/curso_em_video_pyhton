"""
pedra papel tesoura
"""
from random import choice

continuar = 1   # loop
contador = 1
# estilização
estilo = '*' * 25
verde = '\033[1;32m'
vermelho = '\033[1;31m'
limpar = '\033[0;0m'
bold = '\033[1m'
botf = f'{vermelho}Voce perdeu{limpar}, o bot ganhou'
userf = f'{verde}Voce ganhou{limpar}, o bot o perdeu'
print(f'{estilo*2}\n PEDRA, PAPEL e TESOURA\n{estilo*2}')

while continuar == 1:
    print(f'\n  \033[1;33mJOGO : {contador}{limpar}')
    lista = ['pedra', 'papel', 'tesoura']
    print(
        f'  {bold}Faça a escolha :{limpar}\n   1 - pedra\n   2 - papel\n   3 - tesoura'
    )
    userE = int(input(' : '))

    # removendo a escolha do usuario da lista
    if userE == 1:
        lista.remove('pedra')
        userE = 'pedra'
    elif userE == 2:
        lista.remove('papel')
        userE = 'papel'
    elif userE == 3:
        lista.remove('tesoura')
        userE = 'tesoura'

    # bot escolhendo
    bot = choice(lista)
    print(f'  O bot escolheu: {bot}')

    # ganhos do bot
    if bot == 'pedra' and userE == 'tesoura':
        print(f'  {botf}')
    elif userE == 'papel' and bot == 'tesoura':
        print(f'  {botf}')
    elif userE == 'pedra' and bot == 'papel':
        print(f'  {botf}')

    # ganhos do usuario
    elif userE == 'pedra' and bot == 'tesoura':
        print(f'  {userf}')
    elif userE == 'tesoura' and bot == 'papel':
        print(f'  {userf}')
    elif userE == 'papel' and bot == 'pedra':
        print(f'  {userf}')
    continuar = int(input('  \n  (1) - continuar\n  (2) - parar\n  : '))
    contador += 1
# 05/05/2023 9:32Pm
