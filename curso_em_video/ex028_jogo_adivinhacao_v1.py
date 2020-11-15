# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

n = randint(0, 5)

print('-=' * 34)
print('Estou pensando em um número entre 0 e 5, consegue adivinhar qual é?')
print('-=' * 34)

n1 = int(input('Digite o número que eu pensei: '))

print('PROCESSANDO...')
sleep(1.5)

if n == n1:
    print('\nVocê acertou!')
else:
    print('\nVocê errou! Eu pensei no número {} e não no {}.'.format(n, n1))
