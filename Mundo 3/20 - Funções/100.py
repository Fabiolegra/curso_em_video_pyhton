from random import randint


def cem():
    dados = []
    for x in range(5):
        n = randint(1, 101)
        dados.append(n)
    somapar = 0
    for x in dados:
        if x % 2 == 0:
            somapar += x
    return dados, somapar


print(f'  Numeros sorteados: {cem()[0]}\n  Soma dos pares: {cem()[1]}')
# 14/05/2023 4:48Pm
