matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for ll in range(0, 3):
    for cc in range(0, 3):
        matriz[ll][cc] = int(input(f'Digite um valor [{ll},{cc}]: '))

print('-=' * 20)

for ll in range(0, 3):
    for cc in range(0, 3):
        print(f'[{matriz[ll][cc]:^5}]', end='')
    print()
