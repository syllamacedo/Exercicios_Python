lista = []
for n in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {n}: ')),)
print('-=' * 20)
print(f'Você digitou os valores: {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições ', end='')
for p, n in enumerate(lista):
    if n == max(lista):
        print(f'{p}... ', end='')
print(f'\nO menor valor digitado foi {min(lista)} nas posições ', end='')
for p, n in enumerate(lista):
    if n == min(lista):
        print(f'{p}... ', end='')
