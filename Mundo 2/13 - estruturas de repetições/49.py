# tabuada
tabuada = int(input('  Tabuada de qual numero tu desejas : '))
# soma
print('=+=' * 10)
print('  ADIÇÃO')
print('=+=' * 10)
for i in range(1, 11):
    soma = tabuada + i
    print(f'  {tabuada} + {i} = {soma}')
print('=-=' * 10)
print('  SUBTRAÇÃO')
print('=-=' * 10)
# subtração
for e in range(1, 11):
    subtracao = tabuada - e
    print(f'  {tabuada} - {e} = {subtracao}')
print('=×=' * 10)
print('  MULTIPLICAÇÃO')
print('=×=' * 10)
# multiplicação
for m in range(1, 11):
    multi = tabuada * m
    print(f'  {tabuada} × {m} = {multi}')
print('=÷=' * 10)
print('  DIVISÃO')
print('=÷=' * 10)
# divisão
for d in range(1, 11):
    divisao = tabuada / d
    print(f'  {tabuada} ÷ {e} = {divisao:.2f}')
# 06/05/2023 9:47Pm
