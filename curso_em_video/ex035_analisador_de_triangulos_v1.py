print('-=' * 12)
print('Analisador de Triângulos')
print('-=' * 12)

print('\nPasse 3 medidas e descubra se as mesmas conseguem formar um triângulo:')
s1 = float(input('\nPrimeiro Segmento: '))
s2 = float(input('Segundo Segmento: '))
s3 = float(input('Terceiro Segmento: '))

if (s2 - s3) < s1 < s2 + s3 and (s1 - s3) < s2 < s1 + s3 and (s1 - s2) < s3 < s1 + s2:
    print('Os segmentos acima PODEM FORMAR um triângulo.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo.')
