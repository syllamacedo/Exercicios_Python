from time import sleep
num1 = int(input('Digite o 1o numero: '))
num2 = int(input('Digite o 2o numero: '))
opcao = 0

while opcao != 5:
    print('*' * 20)
    print('''O que você deseja fazer?
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
    opcao = int(input('Digite a opção: '))
    if opcao == 1:
        soma = num1 + num2
        print('O resultado da soma entre {} e {} é {}.'.format(num1, num2, soma))
    elif opcao == 2:
        mult = num1 * num2
        print('O resultado da multiplicação entre {} e {} é {}.'.format(num1, num2, mult))
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('Entre {} e {} o maior valor é {}.'.format(num1, num2, maior))
    elif opcao == 4:
        print('Informe os número novamente:')
        num1 = int(input('Digite o 1o numero: '))
        num2 = int(input('Digite o 2o numero: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(1.5)
        print('*' * 20)
    else:
        print('Opção inválida. Tente novamente!')

print('Fim do programa! Volte sempre!')
