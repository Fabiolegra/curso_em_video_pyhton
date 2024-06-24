# mostre o produto e o preçoq
produtos = ('carne', 15, 'peixe', 20, 'ovo', 1, 'missim', 2, 'açucar', 8)
ant = 0
pro = 1
estilo = '--' * 20
print(f'{estilo}\nPRODUTOS E PREÇO\n{estilo}')
for i in produtos:
    print(f'{produtos[ant]:.<25}R$: {produtos[pro]:.2f}')
    if pro > len(produtos) / 2:
        break
    ant += 2
    pro += 2
print('--' * 20)
# 08/05/2023 11:14Pm
