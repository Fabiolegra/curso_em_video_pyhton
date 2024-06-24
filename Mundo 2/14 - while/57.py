"""
se nao fo m ou h repita a pergunta
"""
print(
    """  Sexo:
        [M] - Mulher
        [H] - Homem"""
)
sexo = str(input('  Informe o sexo : ')).upper()
while sexo != 'M' and sexo != 'H':
    sexo = str(input('  Informe o sexo : '))
# 06/05/2023 7:26Pm
