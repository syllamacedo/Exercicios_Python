from random import randint
from time import sleep
from operator import itemgetter
dado = {}
ranking = {}
for n in range(1, 5):
    dado[f'Jogador {n}'] = randint(1, 6)

print(f'{" Valores Sorteados ":=^40}')
for k, v in dado.items():
    print(f'O {k} tirou {v}.')
    sleep(1)

print(f'{" Ranking dos Jogadores ":-^40}')
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}.')
    sleep(1)
