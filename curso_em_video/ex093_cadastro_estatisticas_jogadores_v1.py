dados = dict()
gols_partida = []

dados['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))

for n in range(1, (partidas+1)):
    gols_partida.append(int(input(f'    Quantos gols na partida {n}? ')))

dados['Gols'] = gols_partida.copy()
dados['Total'] = sum(gols_partida)

print('-=' * 30)
for k, v in dados.items():
    print(f'{k}: {v}')

print('-=' * 30)
print(f'O jogador {dados["Nome"]} jogou {partidas} partidas.')

for i, v in enumerate(dados['Gols']):
    print(f'    ==> Na partida {i + 1}, fez {v} gols:')
print(f'Fez um total de {dados["Total"]} gols.')
