"""
aprimora o exercicio 86
"""
matriz = []
cont = 1
while True:
    par = terc = conti = 0
    print('--' * 20)
    print(f'  MATRIZ {cont}')
    print('--' * 20)
    # linha
    for i in range(0, 3):
        if i == 0:
            print('  Primeira fileira')
        elif i == 1:
            print('  Segunda fileira')
        else:
            print('  Terceira fileira')
        # colunas
        for z in range(0, 3):
            num = int(input(f'  Digite o valor {i,z}: '))
            matriz.append(num)
            if z == 2:
                terc += num
            if i == 1:
                if z == 0:
                    maior = num
                else:
                    if num > maior:
                        maior = num

    print('--' * 20)
    for z, x in enumerate(matriz):
        if x % 2 == 0:
            par += x
        print(f'{[x]}', end='')
        if z == 2:
            print(end='\n')
        elif z == 5:
            print(end='\n')
        elif z == 8:
            print(end='\n')
    print('--' * 20)
    print('   ANALISE DE DADOS')
    print('--' * 20)
    print(
        f"""
    [a] - Soma dos pares: {par}
    [b] - Soma terceira coluna: {terc}
    [c] - Maior da 2° linha: {maior}"""
    )
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
    cont += 1
    matriz.clear()
    if continuar == 'N':
        break
print('--' * 20)
# 11/05/2023 8:25Pm
