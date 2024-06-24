def contagem(c, f, p):
    if c > f:
        if p == 0:
            p = -1
        if p > 0:
            p = -p
            f = -1
    if c < f:
        if p == 0:
            p = 1
            f += 1
    print(list(range(c, f, p)))


contagem(1, 10, 1)
contagem(10, 0, 2)
while True:
    começo = int(input('  Iforme o começo: '))
    final = int(input('  Iforme o final: '))
    passo = int(input('  Informe o passo: '))
    contagem(começo, final, passo)
    while True:
        continuar = str(input('  Quer continuar? [S/N]')).upper()[0]
        if continuar not in 'NS':
            print('  DIGITE S PARA SIM E N PARA NÃO')
        else:
            break
    if continuar in 'N':
        break
print(list(range(0, -5, -1)))
# 13/05/2023 11:04Pm
