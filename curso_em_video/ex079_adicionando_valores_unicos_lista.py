listanum = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in listanum:
        listanum.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, já foi adicionado...')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if continuar == 'N':
        break
print('-=' * 20)
listanum.sort()
print(f'Os valores digitados foram: {listanum}')
