# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

peso = float(input('Qual é o seu peso? (kg) '))
alt = float(input('Qual é a sua altura? (ex.: 1.78) '))
imc = peso / (alt ** 2)

if imc < 18.5:
    status = 'ABAIXO DO PESO'
elif 25 >= imc >= 18.5:
    status = 'NORMAL'
elif 30 >= imc > 25:
    status = 'SOBREPESO'
elif 40 >= imc > 30:
    status = 'OBESIDADE'
elif imc > 40:
    status = 'OBESIDADE MÓRBIDA'

print('\nSeu IMC é {:.2f} e está classificado como {}.'.format(imc, status))
