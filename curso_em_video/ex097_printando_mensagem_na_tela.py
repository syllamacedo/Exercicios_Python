def escreva(mensagem):
    tam = len(mensagem) + 2
    print('~' * tam)
    print(f' {mensagem} ')
    print('~' * tam)


texto = str(input('Escreva algo: ')).strip()
escreva(texto)
