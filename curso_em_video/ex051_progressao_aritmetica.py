# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

print('=' * 30)
print('     10 TERMOS DE UMA PA')
print('=' * 30)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

print(termo, ' -> ', end=' ')

for n in range(9):  # o range será 9 pois o usuário já passa o 1o termo, assim fazem 10 no total
    termo = termo + razao
    print(termo, ' -> ', end=' ')

print('ACABOU')
