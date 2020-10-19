print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)

s1 = float(input('Primeiro Segmento: '))
s2 = float(input('Segundo Segmento: '))
s3 = float(input('Terceiro Segmento: '))

if (s2 - s3) < s1 < s2 + s3 and (s1 - s3) < s2 < s1 + s3 and (s1 - s2) < s3 < s1 + s2:
    print('Os segmentos acima PODEM FORMAR um triângulo.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo.')
