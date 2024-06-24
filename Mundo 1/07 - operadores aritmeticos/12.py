"""
desconto
"""
valor = float(input('  Digite o valor da compra: '))
desconto = int(input('  Informe o valor do desconto: '))
descFeito = valor * (desconto / 100)
valorA = valor - descFeito
print(f'  Desconto :  {descFeito:.2f} \n  Preço atual : {valorA:.2f}')
# 30/04/2023 10:22Pm
