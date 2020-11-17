# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número inteiro: '))
primo = 0

print()
for n in range(1, num + 1):
    if num % n == 0:
        primo += 1
        print('\033[31m', end='') # coloca o número em vermelho
    else:
        print('\033[32m', end='')
    print('{} '.format(n), end=' ') # coloca o número em verde

print('\n\n\033[mO número {} foi divisível {} vezes.'.format(num, primo))

if primo > 2:
    print('E por isso ele NÃO É PRIMO!')
elif primo <= 2:
    print('E por isso ele é PRIMO!')
