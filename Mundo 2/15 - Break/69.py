# peça sexo e idade de varias pessoas e sempre pergunte se quer continuar ou não. depois mostre a- quantas pessoas >18 b - quantos homens e c - <20 mulheres quantos
contT = contM = contH = contMI = 0
while True:
    contT += 1
    print('-' * 20, f'\n   {contT}° - PESSOA\n', '-' * 20)
    print(
        """  IFORME O SEXO:
        [M] - Mulher
        [H] - Homem"""
    )
    sexo = str(input(' : ')).upper()
    while sexo != 'M' and sexo != 'H':
        print('  Resposta inválida informe seu sexo\n  Utilize M ou H')
        sexo = str(input(' : ')).upper()
    if sexo == 'H':
        contH += 1
    idade = int(input('  IFORME A SUA IDADE\n : '))
    while 0 < idade > 130:
        print('  Resposta inválida informe sua\n  idade corretamente')
        idade = int(input(' : '))
    if sexo == 'M' and idade < 20:
        contM += 1
    if idade > 18:
        contMI += 1
    while True:
        print(
            """Quer continuar:
            [S] - sim
            [N] - não"""
        )
        opcao = str(input(' : ')).upper()
        if opcao == 'S':
            break
        else:
            break
    if opcao == 'N':
        break
print(
    f"""  DADOS COLETADOS:
    [a] - pessoas maiores que 18 anoz {contMI}
    [b] - homens cadastrados {contH} 
    [c] - Mulheres menores de 20 anos {contM}"""
)
# 06/05/2023 4:54Pm
