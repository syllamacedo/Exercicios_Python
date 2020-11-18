# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

num = cont = -1
soma = 1

while num != 0:
    soma += num
    num = int(input('Digite um número inteiro [0 para parar]: '))
    cont += 1

print('\nA soma dos números digitados é igual a {}.\n'
      'A quantidade de números digitados foi {}.'.format(soma, cont))
