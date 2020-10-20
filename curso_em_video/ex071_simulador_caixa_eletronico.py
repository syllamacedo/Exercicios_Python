print('=' * 30)
print('{:^30}'.format('BANCO COMUM'))
print('=' * 30)
valor = int(input('Qual valor você quer sacar? R$ '))
while True:
    cinquenta = valor // 50
    print(f'Total de {cinquenta} cédulas de R$50.')
    if valor % 50 == 0:
        break
    resto = valor - (cinquenta * 50)
    vinte = resto // 20
    if vinte > 0:
        print(f'Total de {vinte} cédulas de R$20.')
    if resto % 20 == 0:
        break
    resto = resto - (vinte * 20)
    dez = resto // 10
    if dez > 0:
        print(f'Total de {dez} cédulas de R$10.')
    if valor % 10 == 0:
        break
    resto = valor - ((cinquenta * 50) + (vinte * 20) + (dez * 10))
    if resto > 0:
        print(f'Total de {resto} cédulas de R$1.')
    break
