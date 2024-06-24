"""
se tiver CTPS ACRECSTE MAIS DADOs
"""
dicio = {}
dicio['nome'] = str(input('  Informe seu nome : '))
dicio['anoN'] = int(input('  Iforme o ano que nasceste: '))
dicio['CTPS'] = int(input('  Informe sua CTPS [0 = não tenho]: '))
dicio['idade'] = 2023 - dicio['anoN']
if dicio['CTPS'] != 0:
    dicio['anoC'] = int(input('  Informe ano de contratação: '))
    dicio['salario'] = float(input('  Iforme o seu salario: '))
    dicio['aposenta'] = 65 - dicio['idade']
print('--' * 20)
print('  DADOS INFORMADOS')
print('--' * 20)
for k, v in dicio.items():
    print(f' {k} tem o valor {v}')
# 12/05/2023 8:59Pm
