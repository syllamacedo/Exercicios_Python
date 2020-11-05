# o script vai receber como entrada 5 valores inteiros
# ao final vai mostrar quais valores foram digitados
# e a posicao onde estao o menor e maior valores

lista = []

for n in range(5):
    lista.append(int(input(f'Digite um valor inteiro para a posição {n}: ')),)

print('-=' * 20)
print(f'Você digitou os valores: {lista}')
print(f'O maior valor digitado foi {max(lista)} na posição ', end='')

for p, n in enumerate(lista):
    if n == max(lista):
        print(f'{p}... ', end='')

print(f'\nO menor valor digitado foi {min(lista)} na posição ', end='')

for p, n in enumerate(lista):
    if n == min(lista):
        print(f'{p}... ', end='')
