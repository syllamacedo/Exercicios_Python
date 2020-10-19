# Programa que tem como entrada o peso de 6 pessoas
# No final o programa retorna qual foi o maior e o menor peso

maior = menor = peso = 0

for n in range(1, 6):
    peso = float(input('Digite o peso da {}a pessoa: '.format(n)))
    if n == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O maior peso lido foi de {:.1f}kg.\n'
      'O menor peso lido foi de {:.1f}kg.'.format(maior, menor))
