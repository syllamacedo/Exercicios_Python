from math import factorial

num = int(input('Digite um número para saber seu fatorial: '))

print('\nCalculando o fatorial de {}:'
        '\n{}! = '.format(num, num), end='')

# FAZENDO SEM A BIBLIOTECA MATH
# o valor inicial da variavel f sera a variavel num
# dentro do while devemos colocar um if

# f = num
f = factorial(num)

while num > 0:
    print('{}'.format(num), end='')
    print(' x ' if num != 1 else ' = ', end='')
    num -= 1 # deve ser retirado ao usar o if
    
#    if num != 1:
#        num -= 1
#        f *= num
#    else:
#        f *= num
#        num -= 1

print('{}'.format(f))
