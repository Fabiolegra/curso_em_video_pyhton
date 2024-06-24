"""
crie uma tupla com varias palavras
depois
mostre apenas vogais das palavras
"""
palavras = (
    'vasco',
    'Fabio',
    'argel',
    'maria',
    'lamborguine',
    'Sao paulo',
    'desista',
    'voce',
    'eburro',
    'parar',
)
for p in palavras:
    print(f'\n  Na palavra {p} temos : ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end='')
# 08/05/2023 11:23Pm
