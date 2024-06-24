lista = []
for numeros in range(5):
    n = int(input('  Digite um numero: '))
    if numeros == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(lista)
# 11/05/2023 10:42Pm
