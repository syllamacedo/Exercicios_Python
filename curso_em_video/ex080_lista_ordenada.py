# o programa vai receber 5 numeros e conforme sao recebidos, serao colocados em ordem
# apos receber o valor, vai informar em qual posicao o numero esta sendo adicionado
# nao pode ser utilizado o metodo sort

lista = []

for c in range(5):
    n = int(input('Digite um valor inteiro: '))

    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1

print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
