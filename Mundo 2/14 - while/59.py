# soma mukti...
primeiro = float(input('  Digite o primeiro numero : '))
segundo = float(input('  Digite outro valor '))
print(
    """Escolha:
    [1] - Soma
    [2] - multiplicar
    [3] - maior
    [4] - novos numeros
    [5] - sair do programa
"""
)
func = True
while func:
    escolha = int(input('  Escolha entre as opções : '))
    while 1 < escolha > 5:
        print('  Erro escolha as opções entre 1 e 5')
        escolha = int(input('  Escolha : '))
    if escolha == 1:
        soma = primeiro + segundo
        print(f'  A soma entre {primeiro} e {segundo} é {soma}')
    if escolha == 2:
        multiplicar = primeiro * segundo
        print(
            f'  A multiplicação entre {primeiro} e {segundo} é {multiplicar}'
        )
    if escolha == 3:
        if primeiro > segundo:
            print(f'  O numero {primeiro} é maior que o {segundo}')
        elif primeiro == segundo:
            print(f'  O numero {primeiro} e {segundo} são iguais')
        else:
            print(f'  O numero {segundo} é maior que o {primeiro}')
    if escolha == 4:
        primeiro = float(input('  Digite o primeiro numero : '))
        segundo = float(input('  Digite o segundo numero : '))
    if escolha == 5:
        func = False
# 06/05/2023 8:55Pm
