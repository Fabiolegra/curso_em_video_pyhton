"""
ler 7 pessoas e mostre quantos maiores e menores
"""
contMaior = 0
contMenor = 0
for i in range(7):
    ano = int(input('  Informe em que ano voce nasceu : '))
    if 2023 - ano > 21:
        contMaior += 1
    else:
        contMenor += 1
print(
    f"""  Existem :
    Maiores : {contMaior}
    Menores : {contMenor}"""
)
# 06/05/2023 2:38Pm
