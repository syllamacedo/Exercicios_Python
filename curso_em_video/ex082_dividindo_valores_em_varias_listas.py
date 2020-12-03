# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e
# os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

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
