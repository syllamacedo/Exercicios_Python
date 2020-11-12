dados = dict()
golpart = []

dados['nome'] = str(input('Nome do jogador: '))
part = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

for n in range(1, (part+1)):
    golpart.append(int(input(f'    Quantos gols na partida {n}? ')))

dados['gols'] = golpart.copy()
dados['total'] = sum(golpart)

print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')

print('-=' * 30)
print(f'O jogador {dados["nome"]} jogou {part} partidas.')

for i, v in enumerate(dados['gols']):
    print(f'    ==> Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols.')
