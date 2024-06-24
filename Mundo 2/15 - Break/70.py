# nome e preço de produto a - total gasto b - >1000 c - nome do mais barato
total = mil = barato = 0
cont = 1
baraton = ''
while True:
    print('-' * 20, f'\n  {cont}° PRODUTO\n', '-' * 20)
    produto = str(input('  Iforme o nome do produto : '))
    preco = float(input('  Informe o valor do produto : '))
    total += preco
    if cont == 1:
        barato = preco
        baraton = produto
        cont += 1
    else:
        cont += 1
    if preco > 1000:
        mil += 1
    if preco < barato:
        barato = preco
        baraton = produto
    print(
        """  Quer continuar:
        [S] - sim
        [N] - não"""
    )
    opcao = str(input(' : ')).upper()
    if opcao == 'N':
        break
print(
    f"""\n  DADOS COLETADOS:
    [a] - Total dos gastos : {total}
    [b] - Quantidade de produtos maiores que mil : {mil}
    [c] - Nome e preço do produto mais barato {baraton,barato}"""
)
# 07/05/2023 5:12Pm
