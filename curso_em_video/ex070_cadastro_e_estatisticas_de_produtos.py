# o programa vai ler o nome e preço de n produtos
# ao final vai mostrar o total gasto, quantos produtos custam mais de R$1000 e o nome do mais barato

print('-' * 41)
print('{:^41}'.format(' ATACADÃO '))
print('-' * 41)

total = cont = valor = menor = 0
maisbarato = ''

while True:
    nome = str(input('Nome do produto: ')).strip().upper()
    valor = float(input('Valor: R$ '))
    total += valor

    if total == valor or valor <= menor:
        menor = valor
        maisbarato = nome
    if valor > 1000:
        cont += 1

    escolha = ' '

    while escolha not in 'SN':
        escolha = str(input('Deseja continuar [S/N]: ')).strip().upper()

    print()
    if escolha == 'N':
        break

print(f'{" FIM DO PROGRAMA ":=^41}')
print('Total gasto: {:.2f}.\n'
      'Produtos com valor acima de R$ 1.000: {}.\n'
      'Produto mais barato: {}.'.format(total, cont, maisbarato))
