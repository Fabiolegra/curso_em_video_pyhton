# peça um numero em inteiro e imprima por extenso
extenso = (
    'zero',
    'um',
    'dois',
    'tres',
    'quatro',
    'cinco',
    'seis',
    'sete',
    'oito',
    'nove',
    'dez',
    'onze',
    'doze',
    'treze',
    'quatorze',
    'quinze',
    'dezesseis',
    'dezesete',
    'dezoito',
    'dezenove',
    'vinte',
)
print('--' * 20)
while True:
    numero = int(input('  Digite um numero : '))
    while 0 < numero > 20:
        numero = int(input('  Digite um numero : '))
    print(f'  O número {numero} em extenso é {extenso[numero]}')
    print('--' * 20)
    print(
        """  DESEJA CONTINUAR:
    [S] - sim
    [N] - não"""
    )
    continuar = str(input('  : ')).upper()
    print('--' * 20)
    if continuar == 'N':
        print('  Ok, volte sempre')
        break
# 08/05/2023 2:24Pm
