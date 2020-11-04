# o script ao iniciar vai fazer o sorteio de 5 numero de 0 a 10
# depois de mostrar os numeros sorteados, vai indicar o menor e maior valor

from random import randint
from time import sleep

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Os valores sorteados foram: ', end='')

for n in numeros:
    sleep(0.5)
    print(f'{n}', end=' ')

print(f'\nO menor valor sorteado foi {min(numeros)}.\n'
      f'O maior valor sorteado foi {max(numeros)}.')
