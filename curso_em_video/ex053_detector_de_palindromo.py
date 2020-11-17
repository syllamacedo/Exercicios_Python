# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. Exemplos de palíndromos:
# apos a sopa / a sacada da casa / a torre da derrota / o lobo ama o bolo / anotaram a data da maratona

string = str(input('Digite uma palavra ou frase: ')).strip().upper()
letras = string.split()
tudojunto = ''.join(letras)
inverso = ''

definicao = "palavra" if len(letras) == 1 else 'frase'

for l in range(len(tudojunto) - 1, -1, -1):
    inverso += tudojunto[l]

print('\nO inverso de {} é {}.'.format(tudojunto, inverso))

if inverso == tudojunto:
    print('Essa {} é um PALÍNDROMO!'.format(definicao))
else:
    print('A {} digitada NÃO É um palíndromo.'.format(definicao))
