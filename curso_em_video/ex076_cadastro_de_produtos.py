# foi feita uma adaptação nesse exercicio, ao inves de ser uma tupla com valores predeterminados
# o programa vai receber do usuario o cadastro do nome e preco de 5 produtos
# ao final vai exibir a listagem dos mesmos

print('-=' * 20)
print(f'{"Programa de cadastro de Produtos":^40}')
print('-=' * 20)

lista = (str(input('1o Produto: ')),
         float(input('Preço do Produto: ')),
         str(input('2o Produto: ')),
         float(input('Preço do Produto: ')),
         str(input('3o Produto: ')),
         float(input('Preço do Produto: ')),
         str(input('4o Produto: ')),
         float(input('Preço do Produto: ')),
         str(input('5o Produto: ')),
         float(input('Preço do Produto: ')))

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for n in range(0, len(lista)):
    if n % 2 == 0:
        print(f'{lista[n]:.<30}', end='')
    elif n % 2 == 1:
        print(f'R${lista[n]:>7}')
