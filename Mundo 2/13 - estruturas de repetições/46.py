"""
contagem de 10 até 0 com um segundo de diferença entre os nuneros
"""
from time import sleep

print('-=' * 10)
print('  Contagem regressiva')
print('-=' * 10)
for i in range(10, -1, -1):
    sleep(1)
    print(f' CONTAGEM : {i}')
print('  Fim da contagem')
# 06/05/2023 9:29Pm
