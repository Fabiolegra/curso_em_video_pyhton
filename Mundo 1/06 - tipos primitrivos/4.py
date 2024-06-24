"""
faça um programa que peça algo e imprima seu tipo primitivo e todas informações sobre ele
"""
x = str(input('  DIGITE ALGO: '))
print(f' tipo : {type(x)}')
print(f' é um numero? : {x.isnumeric()}')
print(f' é uma letra? : {x.isalpha()}')
print(f'  é uma float? : {x.isdecimal()}')
print(f'  somente em uppercase? : {x.isupper()}')
print(f'  Somente em lowercase? : {x.islower()}')
print(f' é alfanumerico? : {x.isascii()}')
print(f' é digito? :{x.isdigit()}')
print(f'  é verdadeiro? : {x.istitle()}')
# 30/04/2023 9:07Pm
