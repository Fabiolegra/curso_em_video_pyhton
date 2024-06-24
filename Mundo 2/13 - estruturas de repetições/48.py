"""
numeros impares entre 1 500 que são multiplos de 3
"""
cont_impar = 0
for i in range(1, 501):
    if i % 2 != 0:
        if i % 3 == 0:
            print(f'  O numero {i} é multiplo de 3')
            cont_impar += 1
print(
    f'  Existem {cont_impar} numeros impares multiplos de tres que são impares'
)
print('  Fim do programa')
