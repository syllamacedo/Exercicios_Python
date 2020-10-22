# é cobrado valor de R$ 0.50 por Km em viagens de até 200Km e R$ 0.45 em viagens mais longas.

distancia = float(input('Qual será a distância da sua viagem em KM: '))
valor_curta = 0.45
valor_longa = 0.50

if distancia > 200:
    preco = distancia * valor_curta
else:
    preco = distancia * valor_longa
print('O preço da sua passagem será de R$ {:.2f}.'.format(preco))
