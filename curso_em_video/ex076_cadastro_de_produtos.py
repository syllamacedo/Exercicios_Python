print('-='*20)
print('Programa de cadastro de Produtos.\n'
      'INSIRA 5 PRODUTOS:')
print('-='*20)
lista = (str(input('1o Produto: ')),
         str(input('Preço do Produto: ')),
         str(input('2o Produto: ')),
         str(input('Preço do Produto: ')),
         str(input('3o Produto: ')),
         str(input('Preço do Produto: ')),
         str(input('4o Produto: ')),
         str(input('Preço do Produto: ')),
         str(input('5o Produto: ')),
         str(input('Preço do Produto: ')))
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":40}')
print('-'*40)
for n in range(0, len(lista)):
    if n % 2 == 0:
        print(f'{lista[n]:.<30}', end='')
    elif n % 2 == 1:
        print(f'R${lista[n]:>7}')
