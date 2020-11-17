# Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são
# múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = valores = 0

for n in range(1, 501, 2):
    if n % 3 == 0:
        soma = soma + n
        valores = valores + 1

print('A soma dos {} valores é igual a {}.'.format(valores, soma))
