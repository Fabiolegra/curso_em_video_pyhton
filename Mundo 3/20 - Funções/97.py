def escreva():
    texto = str(input('  ESCREVA O TEXTO: '))
    t = len(texto)  # tamanho da string
    print('--' * t)
    print(f'{texto.center(t*2)}')
    print('--' * t)


escreva()
# 13/05/2023 8:26Pm
