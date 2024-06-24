# faça a tabuada de n numeros e pare so quando for negativo
style = 'TABUADA'
print(f'  {style:-^40}')
while True:
    tab = int(input('\n  Tabuada de que numero tu desejas : '))
    if tab > 0:
        print('<<' * 20)
        for i in range(1, 10 + 1):
            mult = tab * i
            print(f'  {tab}×{i} = {mult}')
    else:
        print('  Programa encerrado, adeus baby')
        break
# 07/05/2023 12:48Pm
