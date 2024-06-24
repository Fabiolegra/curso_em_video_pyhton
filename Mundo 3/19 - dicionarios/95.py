cont = 1
jogadores = []

apr = {}
e = '--' * 20
while True:
    gols_lista = []
    print(f'{e}\n  JOGADOR {cont}\n{e}')
    apr['jogador'] = str(input('  Digite o nome do jogador: ')).upper()
    n = int(input('  Quantas partidas jogadas: '))
    apr['partidas'] = n
    for i in range(1, n + 1):
        gols = int(input(f'  {i}° Jogo gols: '))
        apr[f'gols{i}'] = gols
    jogadores.append(apr.copy())
    """
    print('--'*20)
    print(f"  APROVEITAMENTO DO JOGADOR {apr['jogador']}")
    print('--'*20)
    for k,v in apr.items():
        print(f'  {k:.<15}{v}')
    print('--'*20)
    """
    cont += 1
    continuar = str(input('  Deseja continuar? [S/N]')).upper()[0]
    while continuar != 'S' and continuar != 'N':
        print('  digite sim[S] ou não[N]')
    if continuar == 'N':
        break
cont = 0
while True:
    print('0 - encerrar programa')
    numero = int(
        input('  Informe o numero do jogador para ver o rendimento: ')
    )
    for i, x in enumerate(jogadores):
        if i == numero - 1:
            print(f'{e}\nANALISE DE DADOS\n  JOGADOR {i+1}\n{e}')
            for k, v in x.items():
                print(f'{k:.<10}{v}')
    if numero == 0:
        break
print('obrigado')
# 13/05/2023 4:32 Pm
