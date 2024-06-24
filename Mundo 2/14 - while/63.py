# sequencia de fibonacci
func = True
aux = 0
lista = []
numero = int(input(' Digite ate qual da sequencia de fibonacci voce quer : '))
ant = 0
pos = 1
lista.append(ant)
lista.append(pos)
while numero > aux:
    soma = ant + pos
    ant = pos
    pos = soma
    aux += 1
    if len(lista) < numero:
        lista.append(soma)
print(lista)
# 06/05/2023 9:45Pm
