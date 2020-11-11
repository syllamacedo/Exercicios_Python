# o programa vai realizar a soma de valores de um range pre determinado

soma = valores = 0

for n in range(1, 501, 2):
    if n % 3 == 0:
        soma = soma + n
        valores = valores + 1

print('A soma dos {} valores é igual a {}.'.format(valores, soma))
