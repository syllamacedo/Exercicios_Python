# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = somacoluna = maior = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor inteiro para [{linha},{coluna}]: '))

        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]      # soma os numeros pares
        if coluna == 2:
            somacoluna += matriz[linha][coluna]     # soma os valores da 3a coluna
        if linha == 1:
            if matriz[linha][coluna] > maior:
                maior = matriz[linha][coluna]   # guarda o maior valor da 2a linha

print('-=' * 20)

for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
    print()

print(('-=' * 20))
print(f'A soma dos valores pares é {pares}.'
      f'\nO maior valor da 2a linha é {maior}.'
      f'\nA soma dos valores da 3a coluna é {somacoluna}.')
