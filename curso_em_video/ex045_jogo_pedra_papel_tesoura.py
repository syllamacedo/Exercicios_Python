from random import randint
from time import sleep

jokenpo = 'pedra papel tesoura'.upper().split()
pc = randint(0, 2)
print('''Suas opções:
 [ 0 ] PEDRA
 [ 1 ] PAPEL
 [ 2 ] TESOURA''')

jogador = str(input('Qual é a sua jogada? '))
if jogador not in '012':
    print('Escolha dentre uma das opções acima.')
    jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 20)
print('Computador jogou {}'.format(jokenpo[pc]))
print('Jogador jogou {} '.format(jokenpo[jogador]))
print('-=' * 20)

if pc == 0:  # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
elif pc == 1:  # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
if pc == 2:  # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
