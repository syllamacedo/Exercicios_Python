print('GERADOR DE PA')
print('-=' * 10)
num = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
print('-=' * 10)
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(num), end='')
        num += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar mais: '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
