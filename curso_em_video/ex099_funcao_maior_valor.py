# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros
# com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep


def maior(*num):
    contador = maiornum = 0

    print('-=' * 20)
    print('Analisando os valores passados...')

    if num == ():
        print('Não foram informados valores.')
        return

    for n in num:
        print(f'{n}...', end=' ')
        sleep(0.7)

        if contador == 0:
            maiornum = n
        else:
            if n >= maiornum:
                maiornum = n

        contador += 1

    print(f'\nForam informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maiornum}.')


maior(6)
maior(-2, -9, -4, -5, -7, -1)
maior(5, 15, 9, 0, -2)
maior()  # Passando nenhum valor
