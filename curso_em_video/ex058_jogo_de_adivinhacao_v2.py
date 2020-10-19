from random import randint
from time import sleep

numpc = randint(0, 10)
palpites = 0
acertou = False

print('-=' * 20)
print('         DESAFIO DE ADIVINHAÇÃO')
print('-=' * 20)
print('Vou escolher um número de 0 a 10, acha que consegue adivinhar qual vai ser?')
print('.')
sleep(2)
print('.')
sleep(2)
print('.')

while not acertou:
    numjogador = int(input('Qual número você acha que o computador escolheu: '))
    palpites += 1
    if numpc == numjogador:
        acertou = True
    elif numpc != numjogador:
        if numpc > numjogador:
            print('Tente um número maior.')
        else:
            print('Tente um número menor.')

if palpites == 1:
    print('Você ACERTOU DE PRIMEIRA! Você é um Mestre da Adivinhação.')
else:
    print('Você ACERTOU após {} tentativas. PARABÉNS!'.format(palpites))
