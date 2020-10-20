from random import randint
from time import sleep

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Os valores sorteados foram: ', end='')
for n in numeros:
    sleep(0.5)
    print(f'{n}', end=' ')

print(f'\nO menor valor sorteado foi {min(numeros)}.\n'
      f'O maior valor sorteado foi {max(numeros)}.')
