# fatorial
func = True
fatorial = 0
while func:
    user = int(input('  Digite um numero : '))
    aux = user - 1
    while aux != 0:
        soma = user * aux
        fatorial += soma
        aux -= 1
    print(f'  Fatorial de {user} é igual a {fatorial}')
    print(
        """  Deseja inserir outro valor:
        [1] - sim
        [2] - não """
    )
    opcao = int(input(' : '))
    if opcao == 2:
        func = False
    else:
        soma = 0
        fatorial = 0
        user = 0
# 06/05/2023 9:02Pm
