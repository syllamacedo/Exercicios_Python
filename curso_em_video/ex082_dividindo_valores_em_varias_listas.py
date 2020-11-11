# o script vai receber a entrada de n valores inteiros
# ao final vai mostrar a lista completa, lista com numeros pares e lista com numeros impares

listapar, listaimpar = [], []
num = 0

while True:
    num = int(input('Digite um número inteiro: '))

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
print(f'A lista completa é {lista}'
      f'\nA lista de pares é {listapar}'
      f'\nA lista de ímpares é {listaimpar}')
