# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(mensagem):
    tam = len(mensagem) + 2
    print('~' * tam)
    print(f' {mensagem} ')
    print('~' * tam)


texto = str(input('Escreva algo: ')).strip()
escreva(texto)
