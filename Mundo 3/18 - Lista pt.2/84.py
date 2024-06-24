"""
faça uma lista com o peso e a idade de x pessoas e armazene em uma lista
depois:
    a - quantas pessoas foram cadastradas
    b - listagem com as pessoas mais pesadas
    c - e uma com as menos pesadas
"""
lista = []
aux = []
while True:
    aux.append(str(input('  Nome : ')))
    aux.append(float(input('  Peso: ')))
    lista.append(aux[:])
    aux.clear()
    # opção de continuar
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
# Estilo
print('--' * 20)
print('   ANÁLISE DE DADOS')
print('--' * 20)
# Task [A]
print(f'  Pessoas cadastradas : {len(lista)}')
for i, p in enumerate(lista):
    if i == 0:
        maior = menor = 0
        maior = menor = p[1]
    else:
        if maior < p[1]:
            maior = p[1]
        if menor > p[1]:
            menor = p[1]
print('  Pessoas mais pesadas :', end='')
for i, p in enumerate(lista):
    if maior == p[1]:
        print(f' {lista[i][0]},', end='')
print(f' tem {maior} quilos', end='')
print()
print('  Pessoas menos pesadas :', end='')
for i, p in enumerate(lista):
    if menor == p[1]:
        print(f' {lista[i][0]},', end='')
print(f' tem {menor} quilos', end='')
print('--' * 20)
# 11/05/2023 10:08Pm
