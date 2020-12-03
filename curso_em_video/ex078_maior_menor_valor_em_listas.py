# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []

for n in range(5):
    lista.append(int(input(f'Digite um valor inteiro para a posição {n}: ')),)

print('-=' * 20)
print(f'Você digitou os valores: {lista}')
print(f'O maior valor digitado foi {max(lista)} na posição ', end='')

for p, n in enumerate(lista):
    if n == max(lista):
        print(f'{p}... ', end='')

print(f'\nO menor valor digitado foi {min(lista)} na posição ', end='')

for p, n in enumerate(lista):
    if n == min(lista):
        print(f'{p}... ', end='')
