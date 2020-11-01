# o script recebe como entrada uma quantidade x de números
# retorna a media, maior e menor numero digitado

continuar = 'S'
soma = quant = media = maior = menor = 0

while continuar == 'S':
    num = int(input('Digite um número inteiro: '))
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
    print()

    while continuar not in 'SN':
        continuar = str(input('Digite uma opção válida. Deseja continuar [S/N]: ')).strip().upper()[0]

media = soma / quant

print('\nA média entre os números digitados é {:.1f}.\n'
      'O maior número digitado foi {} e o menor foi {}.'.format(media, maior, menor))
