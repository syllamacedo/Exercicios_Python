while True:
    print('-' * 40)
    num = int(input('Qual número deseja ver a tabuada: '))
    print('-' * 40)
    if num < 0:
        break
    for n in range(1, 11):
        print(f'{num} x {n:2} = {num * n:2}')
        n += 1
print('PROGRAMA DE TABUADA ENCERRADO.')
