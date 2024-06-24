"""
Peça a quilometragem rodada e a quantidade de dias locadas
1 dia = 60 R$
1 km = 0,15 R$
"""
dias = int(input('  Quantos dias o carro ficou com voce : '))
km = int(input('  Quantos quilometros foram rodados com voce : '))
total = 60 * dias + km * 0.15
print(f'  Valor a pagar {total}')
# 01/05/2023
