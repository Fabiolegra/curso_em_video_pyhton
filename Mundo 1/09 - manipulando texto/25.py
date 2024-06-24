"""
proucre silva em um nome
"""
nome = str(input('  Digite seu nome : ')).upper().split()
silva = nome.count('SILVA')
if silva > 0:
    tem = 'sim'
else:
    tem = 'não'
print(f'  Seu nome contém silva : {tem}')

print('##outro metodo')

print(f"  Seu nome contém silva : {'SILVA' in nome}")
# 02/04/2023 1:30Pm
