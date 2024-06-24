"""
peça um numero inteiro que escolha entre binario, octal e hexadecimal ou todas opções
"""
inteiro = int(input('  Digite um numero inteiro: '))
print(
    """  Escolha a opção de conversão:
    1 - Binário
    2 - octal
    3 - hexadecimal
    4 - Todas opções"""
)
opcao = int(input('  : '))
if opcao == 1:
    print(f'  O numero {inteiro} em binário : {inteiro:b}')
if opcao == 2:
    print(f'  O numero {inteiro} em octal : {inteiro:o}')
if opcao == 3:
    print(f'  O numero {inteiro} em hexadecimal : {inteiro:x}')
if opcao == 4:
    print(
        f"""  O numero {inteiro} em :
     Binário : {inteiro:b}
     Octal : {inteiro:o}
     Hexadecimal : {inteiro:x}"""
    )

# 05/05/2023 1:03Pm
