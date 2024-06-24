"""
peça duas notas e mostre if foi aprovado or não
"""
nota1 = float(input('  Digite a primeira nota : '))
nota2 = float(input('  Digite a segunda nota : '))
mediaNotas = (nota1 + nota2) / 2
if mediaNotas < 5:
    print('  Reprovado')
elif mediaNotas > 5 and mediaNotas <= 6.9:
    print('  Recuperação')
else:
    print('  Aprovado')
# 05/05/2023 6:10Pm
