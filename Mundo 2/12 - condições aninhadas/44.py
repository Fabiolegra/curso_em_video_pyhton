"""
condições de pagamento
"""
valorP = float(input('  Informe o valor do produto : '))
print(
    '  Forma de Pagamento:\n   1 - dinheiro ou cheque\n   2 - cartão à vista\n   3 - 2x no cartão\n   4 - 3x ou mais no cartão'
)
formaP = int(input('  :  '))
if formaP == 1:
    desconto = valorP * (10 / 100)
    novoP = valorP - desconto
    print(f'  Novo valor : {novoP} desconto em reais {desconto}')
elif formaP == 2:
    desconto = valorP * (5 / 100)
    novoP = valorP - desconto
    print(f'  Novo valor : {novoP} desconto em reais {desconto}')
elif formaP == 3:
    print(f'  Valor : {valorP}')
elif formaP == 4:
    juros = valorP * (20 / 100)
    novoP = valorP + juros
    print(f'  Novo valor : {novoP} juros em reais {juros}')
else:
    print('  erro')
# 05/05/2023 6:52Pm
