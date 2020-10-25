from random import randint
n = randint(0, 5)
print('-=' * 34)
print('Estou pensando em um número entre 0 e 5, consegue adivinhar qual é?')
print('-=' * 34)
n1 = int(input('Digite o número que eu pensei: '))
if n == n1:
    print('\nVocê acertou!')
else:
    print('\nVocê errou! Eu pensei no número {} e não no {}.'.format(n, n1))
