# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

num = (int(input('Digite o 1o número: ')),
       int(input('Digite o 2o número: ')),
       int(input('Digite o 3o número: ')),
       int(input('Digite o 4o número: ')))

print(f'\nVocê digitou os valores {num}.')
print(f'\nO valor 9 apareceu {num.count(9)} vezes.')

if 3 in num:
    print(f'O valor 3 apareceu {num.index(3)+1}a posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')

print('Os valores pares digitados foram: ', end='')

numpar = 0

for n in num:
    if n % 2 == 0:
        numpar += 1
        print(n, end=' ')

if numpar == 0:
    print('nenhum')
