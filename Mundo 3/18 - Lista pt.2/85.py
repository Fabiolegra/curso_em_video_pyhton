"""
crie apenas uma lista e armazene os impares e pares em sublistas
"""
lista = [[], []]
print('--' * 20)
print('   PAR OU IMPAR')
print('--' * 20)
for i in range(0, 7):
    n = int(input(f'  Digite o {i+1}° valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print('--' * 20)
lista[0].sort()
lista[1].sort()
print('  ANALISE DE DADOS')
print('--' * 20)
print(
    f"""
   NUMEROS PARES EM ORDEM CRESCENTE:
     {lista[0]}
   NUMEROS IMPARES EM ORDEM CRESCENTE:
     {lista[1]}"""
)
# 11/05/2023 7:29Pm
