# primo ou não
nao_primo = False
primo = False
n = int(input('  Digite o Numero : '))
for i in range(1, 11):
    if n % i == 0:
        if i != 1 and i != n:
            nao_primo = True
        else:
            primo = True
if nao_primo == True:
    print(f'  O numero {n} não é primo')
else:
    print(f'  O numero {n} é primo')
# 06/05/2023 3:09Pm
