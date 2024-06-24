dados = []


def maior(k):
    """
    O maior numero de uma lista
    """
    maiorx = 0
    for v in dados:
        if v > maiorx:
            maiorx = v
    print(maiorx)


while True:
    x = float(input('  Digite um numero: '))
    dados.append(x)
    while True:
        continuar = str(input('  Quer continuar? [S/N]')).upper()[0]
        if continuar in 'NS':
            break
    if continuar in 'N':
        break
print(f'  O maior numero da sequencia: {dados} é:', end=' ')
maior(dados)
print(help(maior))
# 14/05/2023 4:23Pm
