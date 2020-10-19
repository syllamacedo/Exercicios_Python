print('=-' * 12)
print('Analisador de Triângulos')
print('=-' * 12)

l1 = float(input('Digite o valor do Primeiro Segmento: '))
l2 = float(input('Digite o valor do Segundo Segmento: '))
l3 = float(input('Digite o valor do Terceiro Segmento: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    if l1 == l2 == l3:
        triangulo = 'EQUILÁTERO'
    elif l1 != l2 != l3 != l1:
        triangulo = 'ESCALENO'
    else:
        triangulo = 'ISÓSCELES'
    print('Esses segmentos podem formar um triângulo {}.'.format(triangulo))
else:
    print('Esses segmentos NÃO podem formar um triângulo.')
