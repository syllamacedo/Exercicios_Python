from math import factorial

num = int(input('Digite um número para saber seu fatorial: '))
print('Calculando o fatorial de {}! = '.format(num), end='')
f = factorial(num)

# FAZENDO DE FORMA MATEMÁTICA, SEM A AJUDA DO MATH
# f = 1

while num > 0:
    print('{}'.format(num), end='')
    print(' x ' if num != 1 else ' = ', end='')
    num -= 1
    # f *= num
print('{}'.format(f))
