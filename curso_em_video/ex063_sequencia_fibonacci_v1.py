num = int(input('Quantos termos você quer mostrar: '))
t1, t2 = 0, 1

print('-=' * 20)
print('\n{} -> {}'.format(t1, t2), end='')

cont = 3

while cont <= num:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1

print(' -> FIM')
