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
