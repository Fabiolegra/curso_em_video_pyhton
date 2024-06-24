def area():
    largura = float(input('  IFORME A LARGURA: '))
    comprimento = float(input('  IFORME O COMPRIMENTO: '))
    areax = largura * comprimento
    print(
        f'  A area para a:\n\tlargura: {largura}\n\tcomprimento: {comprimento}\n\té {areax}'
    )


def estilo(texto):
    print('--' * 20)
    print(f'{texto:^20}')
    print('--' * 20)


estilo('AREA DO TERRENO')
area()
estilo('  FIM DO PROGRAMA')
# 13/05/2023 8:18Pm
