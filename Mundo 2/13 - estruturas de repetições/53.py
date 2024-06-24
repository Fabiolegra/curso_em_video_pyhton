# frase de tras pra frente
print('==' * 10)
print('  É palidromo? ')
print('==' * 10)
frase = str(input('  Digite a frase : ')).upper().strip().split()
tamanho = len(frase)
lista = []
inverso = []
for i in range(len(frase)):
    for x in frase[i]:
        lista.append(x)
for t in range(len(lista) - 1, -1, -1):
    inverso.append(lista[t])
if lista == inverso:
    print('  Sim, é um palidromo')
else:
    print('  Não, é um palidromo')
# 06/05/2023 2:28Pm
