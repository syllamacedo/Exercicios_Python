# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('GERADOR DE PA')
print('-=' * 10)

num = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

print('-=' * 10)

cont = 1

while cont <= 10:
    print('{} -> '.format(num), end='')
    num += razao
    cont += 1

print('FIM')
