"""
imc
"""
vermelho = '\033[1;31m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
peso = float(input('  Iforme o seu peso : '))
altura = float(input('  Iforme a sua altura : '))
imc = peso / (altura) ** 2
if imc < 18.5:
    print(f' {vermelho} Abaixo do peso')
elif 25 > imc > 18.5:
    print(f'{verde}  Peso ideal')
elif 30 > imc >= 25:
    print(f'{amarelo}  Sobrepeso')
elif 40 > imc > 30:
    print(f'{vermelho}  Obesidade')
else:
    print(f'{vermelho}  Obesidade morbida')
# 05/05/2023 6:35Pm
