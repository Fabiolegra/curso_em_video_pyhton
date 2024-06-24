subdic = {}
lista = []
soma = 0
e = '--' * 20
while True:
    print(e)
    subdic['NOME'] = str(input('  Informe seu nome: '))
    sexo = str(input('  Informe seu sexo [M or H]: ')).upper()[0]
    while sexo != 'M' and sexo != 'H':
        sexo = str(input('  Informe seu sexo [M or H]: ')).upper()[0]
    subdic['SEXO'] = sexo
    subdic['IDADE'] = int(input('  Informe sua idade: '))
    soma += subdic['IDADE']
    lista.append(subdic.copy())
    print(e)
    continuar = str(input('  Deseja continuar [S or N]: ')).upper()[0]
    while continuar != 'N' and continuar != 'S':
        print('  Valor invalido')
        print('  Digite S para sim or N para não')
        continuar = str(input('  Deseja continuar [S or N]: ')).upper()[0]
    if continuar == 'N':
        break
media = soma / len(lista)
print(f'{e}\n ANALISE DOS DADOS\n{e}')
print(f'  Foram {len(lista)} pessoas cadastradas')
print(f'  A média de idades é {media:.2f}')
print('  Lista de todas mulheres: ', end='')
for p in lista:
    if p['SEXO'] in 'M':
        print(f'{p["NOME"]}', end=' ')
print()
print(f'  Nomes das pessoas com idade acima da média: ', end='')
for x in lista:
    if x['IDADE'] > media:
        print(f'{x["NOME"]}', end=' ')
# 13/05/2023 3:37Pm
