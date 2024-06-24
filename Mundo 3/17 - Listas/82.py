"""
armazene uma lista depois crie mais duas para armazena os numeros pares e impares
"""
lista = []
par = []
impar = []
while True:
    n = float(int(input('  Digite um valor : ')))
    lista.append(n)
    continuar = str(
        input(
            """  Deseja continuar:?
    [S] - sim
    [N] - não
    : """
        )
    ).upper()
    while continuar != 'S' and continuar != 'N':
        print('  Comando invalido')
        continuar = str(
            input(
                """  Deseja continuar:?
    [S] - sim
    [N] - não
    : """
            )
        ).upper()
    if continuar == 'N':
        break
for ns in lista:
    if ns % 2 == 0:
        par.append(ns)
    else:
        impar.append(ns)
d = 'DADOS'
print(f' {d:-^20}  ')
print(f'  Numeros informado:\n   {lista}')
print(f'  Numeros pares :\n   {par}')
print(f'  Numeros impares :\n   {impar}')
print('-' * 20)
# 10/05/2023 10:00Pm
