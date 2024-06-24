"""
digite o nome de uma cidade e diga se começa ou não com santos
"""
cidade = str(input('  Digite o nome da cidade : ')).upper().split()
verificar = cidade[0] == 'SANTO'
print(f"  Começa com 'SANTO': {verificar}")
# 03/05/2023 2:42Pm
