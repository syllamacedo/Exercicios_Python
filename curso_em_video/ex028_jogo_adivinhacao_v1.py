from random import randint
n = randint(0, 5)
print('-=' * 40)
print('Estou pensando em um número entre 0 e 5, consegue adivinhar qual é?')
print('-=' * 40)
n1 = int(input('Digite o número que eu pensei: '))
if n == n1:
    print('Você acertou!')
else:
    print('Você errou! Eu pensei no número {} e não no {}.'.format(n, n1))
