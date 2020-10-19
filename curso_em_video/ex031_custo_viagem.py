d = float(input('Qual será a distância da sua viagem em KM: '))

if d > 200:
    preco = d * 0.45
else:
    preco = d * 0.50
print('O preço da sua passagem será de R$ {:.2f}.'.format(preco))
