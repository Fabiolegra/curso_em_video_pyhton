"""
peça a diatancia <200 preco 0,50 se >200 preço 0,45 por km
"""
distancia = float(input('  Digite a distancia : '))
if distancia < 200:
    print(f'  Valor a ser pago : {distancia*0.5:.2f} reias')
if distancia > 200:
    print(f'  Valor a ser pago : {distancia*0.45:.2f}')
# 03/05/2023 2:59Pm
