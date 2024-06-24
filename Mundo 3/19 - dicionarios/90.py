"""
peça o nome e a media se for maior que 7 estar aprivado else reprovado
"""
situacao = {}
lista = []
e = '--' * 20
n = int(input('  Quantos anlunos a serem cadastrados: '))
for i in range(n):
    print('--' * 20)
    situacao['NOME'] = str(input('  Nome do aluno: '))
    situacao['MEDIA'] = float(input('  Informe a média: '))
    lista.append(situacao.copy())
print(e)
print('  ALUNOS E MEDIA')
print(e)
for z in lista:
    print(z)
    for i, x in z.items():
        if i == 'NOME':
            print(' Nome', end=' ')
        print(f'{x}', end=' ')
        if i == 'MEDIA':
            if x < 7:
                print(' Reprovado', end='\n')
            else:
                print(' aprovado', end='\n')
# 12/05/2023 6:25Pm
