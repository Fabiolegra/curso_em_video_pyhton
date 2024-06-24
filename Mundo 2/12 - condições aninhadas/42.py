"""
mostre que tipo é um triangulo
"""
lado1 = int(input('  Iforme o primeiro lado : '))
lado2 = int(input('  Informe o segundo lado : '))
lado3 = int(input('  Informe o terceiro lado : '))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print('  Triangulo tipo : ')
    if lado1 == lado2 == lado3:
        print('  Equilatero')
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print('  isósceles')
    else:
        print('  Escaleno')
else:
    print('  Não é um triangulo ')
# 05/05/2023 6:20Pm
