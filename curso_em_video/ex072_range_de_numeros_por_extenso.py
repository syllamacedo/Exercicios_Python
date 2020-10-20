numext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
          'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = 22
    while num not in range(0, 21):
        num = int(input('Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {numext[num].capitalize()}.')
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Você quer continuar [S/N]? ')).strip().upper()[0]
    if escolha == 'N':
        break
