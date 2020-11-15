# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distancia = float(input('Qual será a distância da sua viagem em KM: '))
valor_curta = 0.45
valor_longa = 0.50

if distancia <= 200:
    preco = distancia * valor_curta
else:
    preco = distancia * valor_longa

print('\nO preço da sua passagem será de R$ {:.2f}.'.format(preco))
