# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lista, pessoas = [], []
maior = menor = 0
pesado, leve = [], []

while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: KG ')))

    if len(lista) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        elif pessoas[1] < menor:
            menor = pessoas[1]

    lista.append(pessoas[:])
    pessoas.clear()
    continuar = ' '

    while continuar not in 'SN':
        continuar = str(input('Deseja incluir mais pessoas [S/N]? ')).strip().upper()

    if continuar == 'N':
        break

    print()

print('-='*25)
print(f'Foram cadastradas {len(lista)} pessoas.\nO maior peso foi de KG {maior}. Peso de', end='')

cont = cont1 = 0

for p in lista:
    if p[1] == maior:
        if cont >= 1:
            print('e', end='')
        print(f' {p[0]} ', end='')
        cont += 1

print(f'\nO menor peso foi de KG {menor}. Peso de', end='')
for p in lista:
    if p[1] == menor:
        if cont1 >= 1:
            print('e', end='')
        print(f' {p[0]} ', end='')
        cont1 += 1
