# Exercício Python 72: Crie um programa que tenha uma tupla totalmente preenchida com
# uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
          'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:

    num = 22
    while num not in range(21):
        num = int(input('Digite um número entre 0 e 20: '))

    print(f'Você digitou o número {numext[num].capitalize()}.')
    print('-'*30)

    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Você quer continuar [S/N]? ')).strip().upper()[0]

    if escolha == 'N':
        break
