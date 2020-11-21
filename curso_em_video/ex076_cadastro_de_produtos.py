# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

# Mudei o exercício para pedir que o usuário entre com o nome e preço de 5 produtos
# ao invés de ser uma tupla com valores pré-determinados no script

print('-=' * 20)
print(f'{"Programa de cadastro de Produtos":^40}')
print('-=' * 20)

listagem = (str(input('1o Produto: ')),
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

for n in range(0, len(listagem)):
    if n % 2 == 0:
        print(f'{listagem[n]:.<30}', end='')
    elif n % 2 == 1:
        print(f'R${listagem[n]:>7}')
