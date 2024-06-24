"""
peça n numeros e pare ao digitar -1 mostre a media e o maior e menor numeros digitados depois pergunte se ele quer continuar digitar novos numeros
"""
func = True
soma = 0
cont = 0
print(
    """  DIGITE:
    [-1] - Para prograna"""
)
while func:
    numero = int(input('  Informe o numero : '))
    if numero != -1:
        soma += numero
        cont += 1
        media = soma / cont
    else:
        print(f'  Média igual a {media}')
        print(
            """ Deseja continuar:
            [1] - sim
            [2] - não
            [3] - recomeçar"""
        )
        continuar = int(input(' : '))
        if continuar == 2:
            func = False
        elif continuar == 3:
            soma = 0
            media = 0
            cont = 0
# 06/05/2023 10:01Pm
