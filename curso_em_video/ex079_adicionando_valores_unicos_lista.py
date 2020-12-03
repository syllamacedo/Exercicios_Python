# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

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
