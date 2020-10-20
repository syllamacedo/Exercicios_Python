lista = [[], []]

for n in range(1, 8):
    num = int(input(f'Digite o {n}o valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

print('-=' * 25)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram: {lista[0]}\n'
      f'Os valores impares digitados foram: {lista[1]}')

