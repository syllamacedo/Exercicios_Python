# valor aplicado para multa é de R$7,00 por cada Km acima do limite

velocidade = int(input('Qual é a velocidade atual do veículo: '))
valorkm = 7
limite = 80

if velocidade > limite:
    multa = (velocidade - limite) * valorkm
    print('Você está acima do limite de velocidade de {} km/h e foi multado.\n'
          'Você deve pagar uma multa de R$ {}!\n'
          'Dirija com segurança!'.format(limite, multa))
else:
    print('Você está dentro do limite de velocidade de {} km/h.\n'
          'Tenha um bom dia! Dirija com segurança!'.format(limite))
