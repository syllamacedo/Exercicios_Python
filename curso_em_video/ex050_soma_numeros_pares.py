# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
# que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = cont = 0

for n in range(1, 7):
    par = int(input('Digite o {}o valor inteiro: '.format(n)))
    if par % 2 == 0:
        soma += par
        cont += 1

print('Você informou {} número PARES e a soma deles é igual a {}.'.format(cont, soma))
