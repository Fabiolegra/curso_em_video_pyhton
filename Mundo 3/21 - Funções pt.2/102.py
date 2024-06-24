def fatorial():
    n = int(input('  De qual numero tu qures o fatorial? '))
    nx = n
    for i in range(n - 1, 1, -1):
        n = n * i
    print('  Escolha:\n\t[1] - Sim\n\t[0] - Não')
    show = bool(int(input('  Quer mostra o processo? ')))
    if show:
        for i in range(nx, 1, -1):
            if i != 2:
                print(f'{i}', end='x')
            else:
                print(f'{i} = {n}')
    else:
        print(f'  Fatorial de {nx} é {n}')


fatorial()
# 14/05/2023 9:26
