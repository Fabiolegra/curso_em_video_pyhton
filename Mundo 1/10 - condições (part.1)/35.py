"""
é triangulo?
"""
a = int(input('  Digite um lado do triangulo : '))
b = int(input('  Digite outro lado do triangulo : '))
c = int(input('  Digite o ultimo lado do triangulo : '))
soma = a + b
soma2 = b + c
soma3 = c + a
menor = menor2 = 0
"""
var = a - b ; var2 = b - c ; var3 = c - a
if var<0:
    var = b - a
if var2<0:
    var2 = c - b
if var3<0:
    var3 = a - c
"""
if soma > c and soma2 > a and soma3 > c:
    print('  É triangulo')
else:
    print('  não é triangulo')
# 03/05/2023 3:31Pm
