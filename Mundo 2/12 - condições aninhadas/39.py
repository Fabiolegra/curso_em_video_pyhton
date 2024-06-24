"""
peça o ano que nasceu e mostre se já passou da hora ou está na hora ou passou da hora
"""
anoNascimento = int(input('  Digite o ano que voce nasceu : '))
idade = 2023 - anoNascimento
if idade > 17:
    print('  Já passou da hora de se alistar')
elif idade < 17:
    print('  Ainda não é sua vez de se alistar')
else:
    print('  Aliste-se no exercito brasileiro')
# 05/05/2023 6:05Pm
