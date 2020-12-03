# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    lista.append(int(input('Digite um valor inteiro: ')))

    continuar = ' '

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()

    if continuar == 'N':
        break

lista.sort(reverse=True)

print('-=' * 20)
print(f'Foram digitados {len(lista)} número(s).'
      f'\nLista em forma decrescente: {lista}')

print('O valor 5 foi encontrado na lista' if 5 in lista
      else 'O valor 5 não foi encontrado na lista.')
