"""
crie 4 players joguem dados aleatorios guarde em um dicionario e o vencedor é quem tira a soma dos maiores dados
"""
from random import randint

dic = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6),
}
raking = sorted(dic.items(), key=lambda item: item[1], reverse=True)
for k, v in dic.items():
    print(f'  O {k} escolheu {v}')
print('--' * 20)
print('  Rankig')
print('--' * 20)
for k, v in raking:
    cont = 1
    print(f'{cont}° lugar: {k:_<15}:{v}')
    cont += 1
# 12/05/2023 8:10Pm
