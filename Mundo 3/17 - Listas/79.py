"""
peça x valores e armazene em uma lista if ja estiver o valor peça que digite outro valor
"""
e = '--' * 20
lista = []
print(f'{e}\n  ARMAZENAMENTO DE VALORES\n{e}')
while True:
    n = float(input('  Digite um valor : '))
    t = n not in lista
    if t:
        lista.append(n)
        print(f'  O numero {n} foi armazenado')

    while t == False:
        print('  Valor já digitado!!')
        n = float(input('  Informe um novo valor :'))
        t = n not in lista
        if t == True:
            print(f'  O numero {n} foi armazenado')
    continuar = str(
        input(
            """  Deseja continuar?:
            [S] - sim
            [N] - nao
            : """
        )
    ).upper()
    print(e)
    while continuar != 'S' and continuar != 'N':
        print('  Valor invalido')
        continuar = str(
            input(
                """  Deseja continuar?:
            [S] - sim
            [N] - nao
            : """
            )
        ).upper()
    if continuar == 'N':
        break
print(f'  Valores armazenados : {lista}')
# 09/05/2023 9:46Pm
