print('=-' * 12)
print('Analisador de Triângulos')
print('=-' * 12)

print('\nPasse 3 medidas e descubra se as mesmas conseguem formar um triângulo:\n')
s1 = float(input('Digite o valor do Primeiro Segmento: '))
s2 = float(input('Digite o valor do Segundo Segmento: '))
s3 = float(input('Digite o valor do Terceiro Segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    if s1 == s2 == s3:
        triangulo = 'EQUILÁTERO'
    elif s1 != s2 != s3 != s1:
        triangulo = 'ESCALENO'
    else:
        triangulo = 'ISÓSCELES'
    print('\nEsses segmentos podem formar um triângulo {}.'.format(triangulo))
else:
    print('\nEsses segmentos NÃO podem formar um triângulo.')
