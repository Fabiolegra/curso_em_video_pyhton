"""
nome de uma pessoa e mostre o primeiro e o ultimo nome
"""
nome = str(input('  Digite seu nome completo : ')).upper().strip()
nome = nome.split()
print(f'  Primeiro nome : {nome[0]}')
print(f'  Ultimo nome : {nome[-1:][0]}')
# 02/05/2023 1:55Pm
