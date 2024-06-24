"""
peça o ano em que nasceu
"""
ano = int(input('  Digite o ano em que nasceu : '))
idade = 2023 - ano
if idade <= 9:
    print('  Mirim')
elif idade <= 14:
    print('  Infantil')
elif idade <= 19:
    print('  Junior')
elif idade <= 20:
    print('  Senior')
else:
    print('  Master')
# 05/05/2023 6:14Pm
