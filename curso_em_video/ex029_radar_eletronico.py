# Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Qual é a velocidade atual do veículo: '))
valorkm = 7
limite = 80

if velocidade > limite:
    multa = (velocidade - limite) * valorkm
    print('\nVocê está acima do limite de velocidade de {} km/h e foi multado.'
          '\nVocê deve pagar uma multa de R$ {}!'
          '\nDirija com segurança!'.format(limite, multa))
else:
    print('\nVocê está dentro do limite de velocidade de {} km/h.'
          '\nTenha um bom dia! Dirija com segurança!'.format(limite))
