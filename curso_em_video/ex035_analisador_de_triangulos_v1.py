print('-=' * 12)
print('Analisador de Triângulos')
print('-=' * 12)

print('\nPasse 3 medidas e descubra se as mesmas conseguem formar um triângulo:\n')
s1 = float(input('Primeiro Segmento: '))
s2 = float(input('Segundo Segmento: '))
s3 = float(input('Terceiro Segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('\nOs segmentos acima PODEM FORMAR um triângulo.')
else:
    print('\nOs segmentos acima NÃO PODEM FORMAR um triângulo.')
