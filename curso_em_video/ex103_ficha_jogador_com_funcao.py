# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(jog='DESCONHECIDO', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


print('--' * 20)
nome = str(input('Nome do jogador: ')).strip().upper()
n_gols = str(input('Número de gols: '))

if n_gols.isnumeric():
    n_gols = int(n_gols)
else:
    n_gols = 0

if nome == '':
    ficha(gol=n_gols)
else:
    ficha(nome, n_gols)
