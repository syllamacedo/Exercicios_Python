# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

num1 = int(input('Digite o 1o número inteiro: '))
num2 = int(input('Digite o 2o número inteiro: '))
opcao = 0

while opcao != 5:
    print('-=' * 20)
    print('''O que você deseja fazer?
\n[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
    
    opcao = int(input('\nDigite a opção: '))
    print()
    
    if opcao == 1:
        soma = num1 + num2
        print('O resultado da soma entre {} e {} é {}.'.format(num1, num2, soma))
    elif opcao == 2:
        mult = num1 * num2
        print('O resultado da multiplicação entre {} e {} é {}.'.format(num1, num2, mult))
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        elif num1 < num2:
            maior = num2
        if num1 == num2:
            print('Não tem valor maior, pois os números são iguais.')
        else:
            print('Entre {} e {} o maior valor é {}.'.format(num1, num2, maior))
    elif opcao == 4:
        print('Informe os número novamente:')
        num1 = int(input('Digite o 1o numero: '))
        num2 = int(input('Digite o 2o numero: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(1.5)
        print('-=' * 20)
    else:
        print('Opção inválida. Tente novamente!')

print('Fim do programa! Volte sempre!')
