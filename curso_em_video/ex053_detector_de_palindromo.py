string = str(input('Digite uma palavra ou frase: ')).strip().upper()
letras = string.split()
tudojunto = ''.join(letras)
inverso = ''

if len(letras) == 1:
    definicao = 'palavra'
else:
    definicao = 'frase'

for l in range(len(tudojunto) - 1, -1, -1):
    inverso += tudojunto[l]
print('\nO inverso de {} é {}.'.format(tudojunto, inverso))

if inverso == tudojunto:
    print('Essa {} é um PALÍNDROMO!'.format(definicao))
else:
    print('A {} digitada NÃO É um palíndromo.'.format(definicao))
