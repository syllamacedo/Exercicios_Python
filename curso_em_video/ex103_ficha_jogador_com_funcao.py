def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


print('--'*20)
nome = str(input('Nome do jogador: ')).strip()
gols = str(input('Número de gols: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)
