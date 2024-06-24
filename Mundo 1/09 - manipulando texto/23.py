"""
faça um programa que leia de 0 a 9999
"""
numeroS = input('  Digite um numero: ')
print('###por string###')
print(
    f'  MILHAR : {numeroS[0]}\n  CENTENA : {numeroS[1]}\n  DEZENA : {numeroS[2]}\n  UNIDADE : {numeroS[3]}'
)
print('### por numeros ###')
numero = int(numeroS)
milhar = numero // 1000
numero -= 1000 * milhar
centena = numero // 100
numero -= 100 * centena
dezena = numero // 10
numero -= 10 * dezena
unidade = numero
print(
    f'  MILHAR : {milhar}\n  CENTENA : {centena}\n  DEZENA : {dezena}\n  UNIDADE : {unidade}'
)
# 02/05/2023 11:11Pm
