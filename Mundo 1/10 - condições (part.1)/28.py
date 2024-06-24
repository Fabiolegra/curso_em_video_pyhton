"""
imprimar um numero entre 0 e 5 e depois peca que o usuario escreva se acertou ou erro
"""
from random import randint

nComputador = randint(0, 6)
nUsuario = int(input('  Digite um numero entre 0 e 5 : '))
if nComputador == nUsuario:
    print('  PARABENS VOCE ACERTOU')
else:
    print('  VOCE ERROU')
print(f'  NUMERO DO SISTEMA :{nComputador}')
# 03/05/2023 2:48Pm
