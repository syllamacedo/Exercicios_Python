from random import randrange
from time import sleep
jogos = []
quantidade = []
print('-' * 40)
print(f'{"JOGA MEGA SENA":^40}')
print('-' * 40)
qntjogos = int(input('Quantos jogos você vai jogar? '))
print('-' * 40)
while qntjogos > 0:
    while len(quantidade) < 6:
        num = randrange(1, 61)
        if num not in quantidade:
            quantidade.append(num)
    qntjogos -= 1
    quantidade.sort()
    jogos.append(quantidade[:])
    quantidade.clear()

print()
for j in jogos:
    qntjogos += 1
    print(f'Jogo {qntjogos}: {j}')
    sleep(1)
print()
print(f'{" BOA SORTE ":=^40}')
