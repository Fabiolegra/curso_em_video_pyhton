# check idade de voto
def voto():
    idade = int(input('  Digite sua idade: '))
    if 18 > idade > 15 or idade > 65:
        situacao = 'OPCIONAL'
    elif idade >= 18:
        situacao = 'OBRIGATÓRIO'
    if idade < 15:
        situacao = 'NEGADO'
    return situacao


print(f'  Sua situação eleitoral: {voto()}')
# 14/05/2023 5:01Pm
