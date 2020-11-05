# o programa vai pedir ao usuario que digite um valor inteiro
# nao serao aceitos valores duplicados
# ao final sera mostrado de forma ordenada quais valores foram adicionados

listanum = []

while True:
    valor = int(input('Digite um valor inteiro: '))

    if valor not in listanum:
        listanum.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, não será adicionado novamente...')

    continuar = ' '

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()

    if continuar == 'N':
        break

print('-=' * 20)

listanum.sort()

print(f'Os valores digitados foram: {listanum}')
