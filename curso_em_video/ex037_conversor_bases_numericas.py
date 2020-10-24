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
