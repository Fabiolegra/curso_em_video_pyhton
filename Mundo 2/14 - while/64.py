# SOME ATÉ DIGITAR 999
func = True
soma = 0
print('  ==== Digite 999 para encerrar ====')
while func:
    n = float(input('  Digite um numero : '))
    if n == 999:
        soma -= 999
        func = False
    soma += n
print(f'  Soma dos numeros digitados {soma}')
# 06/05/2023 9:50Pm
