continuar = 'S'
soma = quant = media = maior = menor = 0

while continuar == 'S':
    num = int(input('Digite um número: '))
    quant += 1
    soma += num
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    continuar = str(input('Deseja continuar [S/N]: ')).upper()[0]
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Digite uma opção válida. Deseja continuar [S/N]: ')).strip().upper()[0]
media = soma / quant
print('A média entre os números digitados é {:.1f}.\n'
      'O maior número digitado foi {} e o menor foi {}.'.format(media, maior, menor))
