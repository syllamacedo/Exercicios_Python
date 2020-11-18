# Exercício Python 66: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

cont = soma = 0

while True:
    num = int(input('Digite um número (0 para parar): '))

    if num == 0:
        break

    soma += num
    cont += 1

print(f'\nA quantidade de números digitados foi {cont} e a soma total deles equivale a {soma}.')
