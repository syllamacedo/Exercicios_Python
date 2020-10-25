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
