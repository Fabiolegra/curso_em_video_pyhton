"""
peso de 5 pesooas mostre o maior e o menor
"""
maior = menor = 0
for i in range(5):
    peso = float(input('  Digite o seu peso : '))

    if i == 0:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(
    f""" ANALISES DOS PESOS:
    maior: {maior}
    menor: {menor}"""
)
# 06/05/2023 2:44Pm
