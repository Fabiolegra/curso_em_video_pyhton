# 51 repete PA 10 termo e pergunte se quer mais 5
n = 1
aux = 1
lista = []
while True:
    numero = float(input('  Primeiro termo : '))
    number1 = numero
    razao = float(input('  Informe a razão : '))
    while n < 10:
        PA = numero + razao
        numero += PA
        n += 1
        lista.append(PA)
    print(
        f'  Valor da PA com primeiro termo : {number1} e razão : {razao} e igual a {PA}'
    )
    print(f'  Os primeiros 10° termos são:\n {lista}')
    print(
        """  Deseja continuar:
        [1] - sim
        [2] - não """
    )
    try:
        sair = int(input(' : '))
    except:
        print('  Erro ')
    else:
        if sair == 2:
            break
# 06/05/2023 9:25Pm
