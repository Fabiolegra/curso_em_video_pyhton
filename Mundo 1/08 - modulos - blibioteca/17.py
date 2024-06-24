"""
leia os catetos de um triangulo retangulo e mostre o comprimento da hipptenusa
"""
from math import sqrt, pow


def z(x):
    return x**2


cttO = int(input('  Digite o cateto oposto : '))
cttA = int(input('  Digite o cateto adjacente : '))
hipotenusa = z(cttO) + z(cttA)
resultado = sqrt(hipotenusa)
print(
    f'  Dado um triangulo retangulo de catetos {cttO} e {cttA} a hipotenusa vale {resultado:.2f}'
)
# 01/05/2023 5:17Pm
