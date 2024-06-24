matriz = []
cont = 1
while True:
    print('--' * 20)
    print(f'  MATRIZ {cont}')
    print('--' * 20)
    cont += 1
    for i in range(0, 3):
        if i == 0:
            print('  Primeira fileira')
        elif i == 1:
            print('  Segunda fileira')
        else:
            print('  Terceira fileira')
        for z in range(0, 3):
            matriz.append(int(input(f'  Digite o valor {i,z}: ')))
    print('--' * 20)
    print(f'    RESULTADO {i-1}')
    print('--' * 20)
    for z, x in enumerate(matriz):
        print(f'   {[ x ]}', end='')
        if z == 2:
            print(end='\n')
        elif z == 5:
            print(end='\n')
        elif z == 8:
            print(end='\n')
    print('--' * 20)
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
    matriz.clear()
    if continuar == 'N':
        break
print('--' * 20)
# 11/05/2023 7:47Pm
