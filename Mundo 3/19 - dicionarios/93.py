"""
programa para o apriveitamento de um jogador:
    nome, quantas partidas jogadas, gols por partidas, totais de gols
"""
cont = 1
while True:
    print('--' * 20)
    print(f'  JOGADOR {cont}')
    print('--' * 20)
    apr = {}
    gols = 0
    apr['jogador'] = str(input('  Digite o nome do jogador: ')).upper()
    n = int(input('  Quantas partidas jogadas: '))
    apr['partidas'] = n
    for i in range(1, n + 1):
        apr[f'gol_{i}'] = int(input(f'  {i}° Jogo gols: '))
        gols += apr[f'gol_{i}']
    apr['totais gols'] = gols
    print('--' * 20)
    print(f"  APROVEITAMENTO DO JOGADOR {apr['jogador']}")
    print('--' * 20)
    for k, v in apr.items():
        print(f'  {k:.<15}{v}')
    cont += 1
    print('--' * 20)
    continuar = str(input('  Deseja continuar? [S/N]'))
    if continuar in 'Nn':
        break
print('  OBRIGADO')
# 12/05/2023 9:24Pm
