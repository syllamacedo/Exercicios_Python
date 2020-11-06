# o script vai receber como entrada n valores inteiros
# ao final vai mostrar quantos valores foram digitados
# vai coloca-los em ordem descrescente e verificar se o numero 5 foi encontrado

lista = []

while True:
    lista.append(int(input('Digite um valor inteiro: ')))

    cont = ' '

    while cont not in 'SN':
        cont = str(input('Deseja continuar [S/N]? ')).strip().upper()

    if cont == 'N':
        break

lista.sort(reverse=True)

print('-=' * 20)
print(f'Foram digitados {len(lista)} número(s).'
      f'\nLista em forma decrescente: {lista}')

print('O valor 5 foi encontrado na lista' if 5 in lista
      else 'O valor 5 não foi encontrado na lista.')
