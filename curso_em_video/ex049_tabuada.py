num = int(input('Digite um número para saber sua tabuada: '))
print('-=' * 7)
for n1 in range(0, 11):
    print('{} x {:2} = {:2}'.format(num, n1, (n1 * num)))
print('-=' * 7)
