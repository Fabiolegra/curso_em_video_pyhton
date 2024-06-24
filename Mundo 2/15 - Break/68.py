# par ou impar só para quando o jogador perder
from random import randint

ganhos = perca = 0
estilo = ' PAR ou IMPAR'
print(f'{estilo:=^30}')
while True:
    print(' ')
    opcao = str(
        input(
            """  Par ou Impar:
        [P] - PAR
        [I] - IMPAR
        : """
        )
    ).upper()
    while opcao != 'P' and opcao != 'I':
        print('  Digite P ou I')
        opcao = str(input(' Par ou impar? '))
    bot = randint(0, 10)
    user = int(input('  Escolha um numero entre 0 e 10 : '))
    while 0 < user > 10:
        user = int(input('  Escolha um numero entre 0 e 10 : '))
    soma = bot + user
    if soma % 2 == 0:
        if opcao == 'P':
            print(f'  Voce ganhou. o bot escolheu {bot}')
            ganhos += 1
        else:
            print('  Voce perdeu')
            perca += 1
            continuar = int(
                input(
                    """Deseja continuar:
        [1] - sim
        [2] - não"""
                )
            )
            if continuar == 2:
                break
    if soma % 2 > 0:
        if opcao == 'I':
            print(f'  Voce ganhou. o bot escolheu {bot}')
            ganhos += 1
        else:
            perca += 1
            print('  Voce perdeu')
            continuar = int(
                input(
                    """Deseja continuar:
        [1] - sim
        [2] - não
        : """
                )
            )
            if continuar == 2:
                break
print(f'  Voce ganhou {ganhos} partidas e perdeu {perca} partidas')
# 07/05/2023 1:22Pm
