from time import sleep


def contador(i, f, p):
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if p < 0:
        p *= -1

    if p == 0:
        p = 1
    cont = i

    if cont > f:
        while cont > f:
            print(f'{cont}... ', end='')
            cont -= p
            sleep(0.5)
    else:
        while cont <= f:
            print(f'{cont}... ', end='')
            cont += p
            sleep(0.5)

    print('FIM!')


help(contador)
contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')

ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
