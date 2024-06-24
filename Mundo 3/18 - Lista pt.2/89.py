# pylint:disable=W1308
"""
peca nome e duas notas armazene tudo em uma lista mostre a media e depois pergunte se o usuario quer ver as notas individuas de alguem
"""
from time import sleep

e = '--' * 20
amarelo = '\033[1;33m'
vermelho = '\033[1;31m'
fim = '\033[0;0m'
contagem = 1
i = 0
listao = list()
nome = nota1 = nota2 = list()
while True:
    print(e)
    print(f'  {contagem} ° ALUNO')
    print(e)
    contagem += 1
    nome = (
        str(input('  Digite o {}nome do aluno{}: '.format(amarelo, fim)))
        .upper()
        .strip()
    )
    nota1 = float(
        input(
            '  Digite a {}primeira nota{} do aluno {}{}{} \n  : '.format(
                amarelo, fim, vermelho, nome, fim
            )
        )
    )
    nota2 = float(
        input(
            '  Digite a {}segunda nota{} do aluno {}{}{} \n  : '.format(
                amarelo, fim, vermelho, nome, fim
            )
        )
    )
    listao.append([nome, nota1, nota2])
    i += 1

    continuar = str(
        input(
            """  Deseja continuar:
        [S] - sim
        [N] - não
        : """
        )
    ).upper()
    while continuar != 'S' and continuar != 'N':
        print('  Comando invalido')
        continuar = str(
            input(
                """  Deseja continuar:
        [S] - sim
        [N] - não
        : """
            )
        ).upper()

    if continuar == 'N':
        break
sleep(2)
print(e)
print(' N°- nome              media')
for i, x in enumerate(listao):
    media = (x[1] + x[2]) / 2
    print(f' {i+1} - {x[0]:<15}   {media:.2f}')
while True:
    print(e)
    continuar = str(
        input(
            """  Quer ver as notas de algum aluno:
        [S] - sim
        [N] - não
        : """
        )
    ).upper()
    while continuar != 'S' and continuar != 'N':
        print('  Comando invalido')
        continuar = str(
            input(
                """  Quer ver mais informação de algum aluno?
        [S] - sim
        [N] - não
        : """
            )
        ).upper()
    if continuar == 'N':
        break
    if continuar == 'S':
        numeracao = int(input('  Digite a numeração do aluno: '))
        numeracao -= 1
        sleep(2)
        print(e)
        print('  MAIS DADOS DO ALUNO ')
        print(e)
        print(f'  Nome: {listao[numeracao][0]}')
        print(f'  NOTA 1°: {listao[numeracao][1]}')
        print(f'  NOTA 2°: {listao[numeracao][2]}')
        sleep(2)
        numeracao += 1
# 11/05/2023 11:49Pm
