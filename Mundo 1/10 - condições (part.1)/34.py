"""
pergunte o salario:
    if >1250 aumento 10%
    if <=1250 aumento 15%
"""
salario = float(input('  Iforme seu salario : '))
if salario > 1250:
    NewS = salario * (10 / 100) + salario
    print(f'  Seu novo salario {NewS} reais')
if salario <= 1250:
    NewS = salario * (15 / 100) + salario
    print(f'  Seu novo salario {NewS}')
# 03/05/2023 3:10Pm
