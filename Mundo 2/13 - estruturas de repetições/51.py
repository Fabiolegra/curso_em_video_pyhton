# Pa e Pg
primeiroT = float(input('  Informe o primeiro termo : '))
razao = int(input('  Informe a razão : '))
primeiroPG = primeiroT
print('+=' * 10, '\n   PA\n', '+=' * 10)
for i in range(0, 10):
    PA = primeiroT + razao
    primeiroT = PA
    print(f'  {i+1}° termo : {PA}')
print('*=' * 10, '\n   PG\n', '*=' * 10)
for x in range(0, 10):
    PG = primeiroPG * razao
    primeiroPG = PG
    print(f'  {x+1}° termo : {PG}')
# 06/05/2023 10:04Pm
