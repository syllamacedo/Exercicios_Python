n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
maior = n1
menor = n1

if n2 >= n1:
    maior = n2
if n3 >= n2:
    maior = n3
if n2 <= n1:
    menor = n2
if n3 <= n2:
    menor = n3

print('O maior número digitado foi {} e o menor foi {}.'.format(maior, menor))
