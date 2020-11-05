# foi feita uma adaptação nesse exercicio, ao inves de ser uma tupla com palavras
# o programa vai pedir que o usuario digite 3 palavras
# e ao final vai mostrar quantas vogais tem em cada uma

print(f'{"Contador de Vogais":^30}')
print('-=' * 15)

palavras = (str(input('Digite a 1a palavra: ')),
            str(input('Digite a 2a palavra: ')),
            str(input('Digite a 3a palavra: ')))

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')

    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
