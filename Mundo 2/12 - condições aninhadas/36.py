"""
emprestimo bancario o programa pergunta:
    a - valor da casa
    b - o salario do comoprador
    c - quantos anos a pagar
a mensalidade deve ser <=30 do salario
"""
estilo = '\033[1;33m'  # bold + amarelo
estilof = '\033[1;0m'   # bold - amarelo
vermelho = '\033[1;31m'
azul = '\033[1;34m'
valor_da_casa = float(input(f'  Informe o {estilo}valor da casa{estilof} : '))
salario = float(input(f'  Informe o {estilo}salario do comprador{estilof} : '))
anos = float(input(f'  Informe {estilo}quantos anos a pagar{estilof} : '))

mensalidade = valor_da_casa / (12 * anos)
max_parcela = salario * (30 / 100)

if max_parcela > mensalidade:
    print('  Máxima parcela = 30% do seu sálario')
    print(
        f'  {estilo}Mensalidade{estilof}: {mensalidade:.2f}\n  {estilo}Máxima parcela{estilof}:{max_parcela}'
    )

anos_temp = anos
if mensalidade > max_parcela:
    print(
        f'  A parcela não poderá ser maior que {vermelho}30% do salario{estilof}'
    )
    print(f'  máx parcela com base no seu sálario : {max_parcela}')

    while mensalidade > max_parcela:
        anos_temp += 1
        mensalidade = valor_da_casa / (12 * anos_temp)
    print(
        f'  {estilo}Voce poderá pagar{estilof}: {azul}{mensalidade:.2f}{estilof} {estilo}por{estilof} {azul}{anos_temp:.0f}{estilof} {estilo}anos{estilof}'
    )
# 05/05/2023 12:50Pm
