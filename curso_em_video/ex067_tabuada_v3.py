# Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:

    print('-=' * 25)
    num = int(input('Qual número deseja ver a tabuada [número negativo para encerrar]: '))
    print('-=' * 25)

    if num < 0:
        break
    for n in range(1, 11):
        print(f'{num} x {n:2} = {num * n:2}')
        n += 1

print('PROGRAMA DE TABUADA ENCERRADO.')
