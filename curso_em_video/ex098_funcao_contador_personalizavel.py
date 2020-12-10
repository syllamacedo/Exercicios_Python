# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
# início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep


def contador(i, f, p):
    if p == 0:
        print('Zero não é aceito como passo. Tente novamente.')
        return

    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if p < 0:
        p *= -1

    cont = i

    if cont > f:
        while cont > f:
            print(f'{cont}... ', end='')
            cont -= p
            sleep(0.7)
    else:
        while cont <= f:
            print(f'{cont}... ', end='')
            cont += p
            sleep(0.7)

    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)

print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')

ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
