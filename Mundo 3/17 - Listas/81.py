"""
peça x numeros mostre quantos foram digitados e em ordem decrescente e se o valor 5 foi digitado
"""
e = '--' * 20
lista = []
while True:
    n = int(input('  Digite um valor : '))
    lista.append(n)
    continuar = str(
        input(
            """ Deseja continuar:
        [S] - Sim
        [N] - não
        :"""
        )
    ).upper()
    print(e)
    while continuar != 'S' and continuar != 'N':
        print('  Valor invalido')
        print('  Só aceitamos S ou N')
        continuar = str(
            input(
                """ Deseja continuar:
        [S] - Sim
        [N] - não
        :"""
            )
        ).upper()
        print(e)
    if continuar == 'N':
        break
lista.sort(reverse=True)
cont = len(lista) + 1
cinco = lista.count(5)
if cinco > 0:
    cinc = 'apareceu'
else:
    cinc = 'NÃO APARECEU'
print(f'  FORAM {cont} digitados')
print(f'  Valores digitados em ordem descrescente: {lista}')
print(f'  O numero cinco {cinc} {cinco} vezes')
# 08/05/2023 10:21Pm
