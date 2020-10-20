matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = somacoluna = maior = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha},{coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:  # SOMA OS NUMEROS PARES
            pares += matriz[linha][coluna]
        if coluna == 2:
            somacoluna += matriz[linha][coluna]
        if linha == 1:
            if matriz[linha][coluna] > maior:
                maior = matriz[linha][coluna]

print('-=' * 20)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
    print()

print(('-=' * 20))
print(f'A soma dos valores pares é {pares}.\n'
      f'O maior valor da 2a linha é {maior}.\n'
      f'A soma dos valores da 3a coluna é {somacoluna}.')
