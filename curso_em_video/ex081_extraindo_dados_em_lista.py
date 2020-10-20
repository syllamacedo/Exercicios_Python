lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if cont == 'N':
        break
lista.sort(reverse=True)
print('-=' * 20)
print(f'Foram digitados {len(lista)} números.\n'
      f'Lista em forma decrescente: {lista}')
print('O valor 5 foi encontrado na lista' if 5 in lista
      else 'O valor 5 não foi encontrado na lista.')
