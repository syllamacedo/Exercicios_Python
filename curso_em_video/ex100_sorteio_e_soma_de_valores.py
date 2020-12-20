# Exercício Python 100: Faça um programa que tenha uma lista chamada números e
# duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e
# a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep


def sorteia(lst):
    print('Sorteando 5 valores da lista: ', end='')

    for cont in range(5):
        n = randint(1, 10)
        lst.append(n)
        print(f'{n}', end=' ')
        sleep(0.5)

    print('PRONTO!')


def somapar(lst):
    soma = 0

    for cont in lst:
        if cont % 2 == 0:
            soma += cont

    print(f'Somando os valores pares de {lst}, temos {soma}.')


numeros = []
sorteia(numeros)
somapar(numeros)
