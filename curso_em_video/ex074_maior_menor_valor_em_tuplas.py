# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
from time import sleep

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Os valores sorteados foram: ', end='')

for n in numeros:
    sleep(0.5)
    print(f'{n}', end=' ')

print(f'\nO menor valor sorteado foi {min(numeros)}.\n'
      f'O maior valor sorteado foi {max(numeros)}.')
