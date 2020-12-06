# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

dado = {}
ranking = []

for n in range(1, 5):  # mudar o alcance do range para aumentar/diminuir o numero de jogadores
    dado[f'Jogador {n}'] = randint(1, 6)

print(f'{" Valores Sorteados ":=^40}')

for k, v in dado.items():
    print(f'O {k} tirou {v}.')
    sleep(1)

print()
print(f'{" Ranking dos Jogadores ":-^40}')

ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}.')
    sleep(1)
