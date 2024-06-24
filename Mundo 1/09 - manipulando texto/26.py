"""
peça uma frase:
    a- mostre quantos "A" aparecem
    b - mostre a posiçãodo primeiro e ultimo "A"
"""
frase = str(input('  Digite uma frase : ')).strip().upper()
print(f"  Quantos 'A' tem na frase : {frase.count('A')}")
print(f"  Qual é a posição do primeiro 'A' : {frase.find('A')}")
print(f"  Qual é a posição do ultimo 'A' : {frase.rfind('A')}")
# 02/05/2023 1:45Pm
