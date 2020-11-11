# o programa faz a simulacao de um jogo de pedra, papel e tesoura
# recebe como entrada qual a opcao o usuario deseja jogar
# faz a simulacao do jogo e ao final mostra quem venceu (computador ou usuario)

from random import randint
from time import sleep

jokenpo = 'pedra papel tesoura'.upper().split()
pc = randint(0, 2)

print('''Suas opções:
 [ 0 ] PEDRA
 [ 1 ] PAPEL
 [ 2 ] TESOURA''')

jogador = int(input('\nQual é a sua jogada? '))

if jogador not in range(3):
    print('Escolha dentre uma das opções acima.')
    jogador = int(input('\nQual é a sua jogada? '))

print('\nJO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 12)
print('Computador jogou {}'.format(jokenpo[pc]))
print('Jogador jogou {} '.format(jokenpo[jogador]))
print('-=' * 12)

if pc == 0:  # computador jogou PEDRA
    if jogador == 0:
        print('\nEMPATE')
    elif jogador == 1:
        print('\nJOGADOR VENCE')
    elif jogador == 2:
        print('\nCOMPUTADOR VENCE')

if pc == 1:  # computador jogou PAPEL
    if jogador == 0:
        print('\nCOMPUTADOR VENCE')
    elif jogador == 1:
        print('\nEMPATE')
    elif jogador == 2:
        print('\nJOGADOR VENCE')

if pc == 2:  # computador jogou TESOURA
    if jogador == 0:
        print('\nJOGADOR VENCE')
    elif jogador == 1:
        print('\nCOMPUTADOR VENCE')
    elif jogador == 2:
        print('\nEMPATE')
