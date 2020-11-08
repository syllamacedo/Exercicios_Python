# o script vai receber valores inteiros para as respectivas posicoes de uma matriz
# a matriz tera 3 linhas e 3 colunas
# ao final vai ser mostrado ao usuario como ficou a disposição da matriz com os valores

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor inteiro para [{linha},{coluna}]: '))

print('-=' * 20)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
