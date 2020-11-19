# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

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
