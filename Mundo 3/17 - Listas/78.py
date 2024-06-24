"""
peça 5 numeros armazene em uma lista e mostre maior e o menor e a posição
"""
lista = []
print('--' * 20)
print('  INFORME 5 NUMEROS')
print('--' * 20)
for x in range(0, 5):
    lista.append(int(input((f'  Informe o {x+1}° valor : '))))
    if x == 0:
        maior = menor = lista[0]
    else:
        if lista[x] > maior:
            maior = lista[x]
        if lista[x] < menor:
            menor = lista[x]
print('--' * 20)
print('  ANALISE DE DADOS  ')
print('--' * 20)
print(f'  Valores informados :{lista}')
print(f'  O maior valor é {maior} e sua posição: ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i+1}...', end='')
print()
print(f'  O menor valor é {menor} e está na posição: ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i+1}...', end='')
# 09/05/2023 9:20Pm - 11/05/2023 5:05Pm
