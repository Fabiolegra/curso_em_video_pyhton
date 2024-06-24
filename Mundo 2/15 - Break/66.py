"""
peca varios numeros até a dihitação de 999 e mostre quantos numeros foram digitados e a soma
"""
soma = cont = 0
while True:
    n = float(input('  Digite um numero : '))
    if n != 999:
        soma += n
        cont += 1
    else:
        break
print(f'  Foram digitados {cont} numeros\n  A soma dos numeros é {soma}')
# 07/05/2023 12:39Pm
