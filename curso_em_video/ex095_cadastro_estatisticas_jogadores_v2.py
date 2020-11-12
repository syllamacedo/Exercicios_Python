dados = dict()
dadosfinal = []

while True:
    golspart = []
    dados['nome'] = str(input('Nome do jogador: ')).upper()
    part = int(input('Quantas partidas ele jogou? '))

    for p in range(part):
        golspart.append(int(input(f'    Quantos gols na partida {p+1}? ')))

    dados['gols'] = golspart[:]
    dadosfinal.append(dados.copy())

    while True:
        resp = str(input('Deseja continuar? [S/N] ')).upper()[0]

        if resp in 'SN':
            break
        print('ERRO! Digite S para sim ou N para não.')

    if resp == 'N':
        break

print('-='*30)
print('cod          ', end=' ')

for i in dados.keys():
    print(f'{i:<15}', end='')

print()
for k, v in enumerate(dadosfinal):
    print(f'{(k+1):>3}', end='')

    for d in v.values():
        print(f'{str(d):>15}', end='')
    print()

while True:
    print('--' * 30)
    mostra = (int(input('Mostrar dados de qual jogador? (999 para sair) ')))

    if mostra == 999:
        break

    if mostra > len(dadosfinal) or mostra <= 0:
        print(f'ERRO! Não existe jogador com código {mostra}! Tente Novamente.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {dadosfinal[mostra - 1]["nome"]}:')
        for k, v in enumerate(dadosfinal[mostra - 1]['gols']):
            print(f'   No jogo {k + 1} fez {v} gols.')

print('<< VOLTE SEMPRE >>')
