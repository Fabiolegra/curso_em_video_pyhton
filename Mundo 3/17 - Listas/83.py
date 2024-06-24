"""
conferir se os colchetes estão fechados
"""
lista = []
while True:
    n = str(input('  Informe a expressão : ')).strip()
    lista = list(n)
    d = lista.count('(')
    l = lista.count(')')
    if d > 0 or l > 0:
        if d == l:
            print('  Expressão sem erros')
        else:
            print('  Expressão com erros')
    else:
        print('  Não é uma expressão')

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
# 10/05/2023 10:50Pm
