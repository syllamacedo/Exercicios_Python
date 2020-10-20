listapar = []
listaimpar = []
num = 0
while True:
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if cont == 'N':
        break
lista = listapar + listaimpar
print('-=' * 25)
print(f'A lista completa é {lista}\n'
      f'A lista de pares é {listapar}\n'
      f'A lista de ímpares é {listaimpar}')
