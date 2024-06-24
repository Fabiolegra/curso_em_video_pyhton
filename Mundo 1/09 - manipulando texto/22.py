"""
leia um nome escreva em maiusculo, minusculo e a quantidade de letras sem espaços
"""
nome = input('  Digite seu nome completo : ')
print(f'  Seu nome em maiuculo : {nome.upper()}')
print(f'  Seu nome em minuscuoo : {nome.lower()}')
espaços = nome.count(' ')
letras = len(nome)
print(f'  Quantidade de letras que tem seu nome : {letras-espaços}')
p_nome = nome.split()
primeiro_nome = p_nome[0]
primeiro_nome = len(primeiro_nome)
print(f'  Quantidade de letras que tem seu primeiro nome: {primeiro_nome}')
# 02/05/2023 1:00Pm
