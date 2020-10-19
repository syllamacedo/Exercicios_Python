vel = int(input('Qual é a velocidade atual do veículo: '))

if vel > 80:
    print('Você está acima do limite de velocidade de 80 km/h e foi multado.\n'
          'Você deve pagar uma multa de R$ {}!\n'
          'Dirija com segurança!'.format(((vel - 80) * 7)))
else:
    print('Você está dentro do limite de velocidade de 80 km/h.\n'
          'Tenha um bom dia! Dirija com segurança!')
