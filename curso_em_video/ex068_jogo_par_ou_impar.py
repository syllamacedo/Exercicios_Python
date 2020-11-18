# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randrange

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')

cont = 0

while True:
    print('=-' * 15)

    jogador = int(input('Digite um valor [ 0 a 10 ]: '))
    escolha = ' '

    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]

    computador = randrange(11)
    soma = jogador + computador

    print(f'\nVocê jogou {jogador} e o computador {computador}, total de {soma}.', end=' ')
    print('Deu PAR.' if soma % 2 == 0 else 'Deu ÍMPAR.')
    print('=-' * 15)

    if (escolha == 'P' and soma % 2 == 1) or (escolha == 'I' and soma % 2 == 0):
        break

    print('Você VENCEU!\n'
          'Vamos jogar novamente...')

    cont += 1

print(f'GAME OVER! '
      f'Você venceu {cont} vezes.')
