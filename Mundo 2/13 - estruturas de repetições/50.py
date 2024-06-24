"""
peça 6 numeros e some somente os pares
"""
somaPares = somaImpares = 0
for i in range(0, 6):
    n = int(input('  Digite um numero : '))
    if n % 2 == 0:
        somaPares += n
    else:
        somaImpares += n
print(
    f"""  SOMA PARES: {somaPares}
  SOMA IMPARES {somaImpares}"""
)
# 06/05/2023 9:53Pm
