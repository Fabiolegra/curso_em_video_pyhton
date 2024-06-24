from time import sleep

"""
tupla do brasileirao:
    a - os primeiro apenas os 5
    b - os 4 ultimos
    c - time em ordem alfabetica
    d - onde está do vasco
"""
style = '==' * 20
brasileiro = (
    'Botafogo',
    'Palmeiras',
    'cruzeiro',
    'Fortaleza',
    'São Paulo',
    'Fluminense',
    'Gremio',
    'Internacional',
    'Bahia',
    'atletico paranaense',
    'Vasco',
    'Brangatino',
    'Cuiabá',
    'Santos',
    'Atletico Mineiro',
    'Flamengo',
    'Corinthias',
    'Góias',
    'Coritiba',
    'América mineiro',
)
print(style)
print('  TABELA DO BRASILEIRÃO SERIE A')
print('  DATA = 08/05/2023')
sleep(1)
for pos, time in enumerate(brasileiro):
    print(f'  {pos+1} - {time}')
print(style)
print(' DADOS : ')
print(style)
print(f'  OS 5 PRIMEIROS :')
sleep(1)
for pos in range(0, 5):
    print(f'  {pos+1} - {brasileiro[pos]}')
print(style)
print(f'  OS 4 ULTIMOS : ')
sleep(1)
for pos in range(16, 20, +1):
    print(f'  {pos+1} - {brasileiro[pos]}')
print(style)
print('  TIMES EM ORDEM ALFABETICA :')
sleep(1)
for pos, time in enumerate(sorted(brasileiro)):
    print(f'  {pos} - {time}')
print(style)
print('  POSIÇÃO DO TIME DO VASCO')
vasco = brasileiro.index('Vasco') + 1
print(f'  {vasco}')
# 08/05/2023 3:01Pm
