# 51 repete PA 10 termo e pergunte se quer mais 5
func = True
n = 1
aux = 1
lista = []
while func:
    numero = float(input('  Primeiro termo : '))
    number1 = numero
    razao = float(input('  Informe a razão : '))
    while n < 10:
        PA = numero + razao
        numero += PA
        n += 1
        lista.append(PA)
    print(
        """Quer mais termos:
        [1] - sim
        [2] - não"""
    )
    opcao = int(input(' : '))
    if opcao == 1:
        m = int(input('  Quantos mais? '))
        while aux < m:
            PA = numero + razao
            numero += PA
            aux += 1
            lista.append(PA)
            if aux == m:
                print(
                    f'  Valor da PA com primeiro termo : {number1} e razão : {razao} e igual a {PA}'
                )
                print(f'  Os primeiros {10+m} termos são:\n {lista}')
    else:
        print(
            f'  Valor da PA com primeiro termo : {number1} e razão : {razao} e igual a {PA}'
        )
        print(f'  Os primeiros 10° termos são:\n {lista}')
    print(
        """  Deseja continuar:
        [1] - sim
        [2] - não """
    )
    sair = int(input(' : '))
    if sair == 2:
        func = False
# 06/05/2023 9:21Pm
