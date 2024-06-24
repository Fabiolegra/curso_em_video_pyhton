maior = 0
contM = 0
somaIH = 0
maiorS = ' '
for i in range(4):
    print(
        """  SEXO:
        [1] - homem
        [2] - mulher """
    )
    sexo = int(input('  Informe seu sexo : '))
    nome = str(input('  Informe seu nome : '))
    ano = int(input('  Informe sua idade : '))
    print(' ')
    somaIH += ano
    media = somaIH / 4
    if sexo == 1:
        if ano > maior:
            maiorS = nome
    if sexo == 2:
        if 20 > ano:
            contM += 1
print(
    f"""ANALISE DE DADOS:
       [1] - Média do grupo {media}
       [2] - Homem mais velho {maiorS}
       [3] - Quantidade de mulheres menores que 20 anos {contM}"""
)
# 06/05/2023 3:02Pm
