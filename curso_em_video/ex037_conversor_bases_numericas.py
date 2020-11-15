# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número inteiro: '))

print('''\nEscolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

opcao = int(input('\nSua opção: '))

if opcao == 1:
    print('\n{} convertido para BINÁRIO é igual a {}.'.format(num, bin(num)))
elif opcao == 2:
    print('\n{} convertido para OCTAL é igual a {}.'.format(num, oct(num)))
elif opcao == 3:
    print('\n{} convertido para HEXADECIMAL é igual a {}.'.format(num, hex(num)))
else:
    print('\nOpção inválida.')
