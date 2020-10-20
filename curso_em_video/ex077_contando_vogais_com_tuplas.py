palavras = (str(input('Digite uma palavra: ')),
            str(input('Digite outra palavra: ')),
            str(input('Digite a última palavra: ')))

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
