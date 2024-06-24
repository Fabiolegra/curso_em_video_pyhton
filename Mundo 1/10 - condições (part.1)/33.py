"""
maior e menor de 3 numeros
"""
maior = menor = 0
for i in range(0, 3):
    n = float(input('  Digite um numero : '))
    if i == 0:
        maior = n
        menor = n
    if menor > n:
        menor = n
    if n > maior:
        maior = n
print(f'  Maior : {maior}  \n  Menor : {menor}')
# 03/05/2023 3:05Pm
