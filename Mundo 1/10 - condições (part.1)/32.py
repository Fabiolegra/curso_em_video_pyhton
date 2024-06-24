"""
verifique se o ano é bissexto
"""
ano = int(input('  Digite o ano : '))
if ano % 4 == 0 and ano % 100 != 0:
    print(f'  O ano {ano} é bissexto')
if ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
    print(f'  O ano {ano} é bissexto')
elif ano % 4 != 0:
    print('  Não é um ano bissexto')
# 03/05/2023
