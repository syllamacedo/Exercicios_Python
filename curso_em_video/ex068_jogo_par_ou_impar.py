from random import randint
print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
cont = 0

while True:
    print('=-' * 15)
    jogador = int(input('Digite um valor: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('-' * 30)
    computador = randint(0, jogador + 1)
    soma = jogador + computador
    print(f'Você jogou {jogador} e o computador {computador}, total de {soma}.', end=' ')
    print('Deu PAR.' if soma % 2 == 0 else 'Deu ÍMPAR.')
    print('-' * 30)
    if (escolha == 'P' and soma % 2 == 1) or (escolha == 'I' and soma % 2 == 0):
        break
    print('Você VENCEU!\n'
          'Vamos jogar novamente...')
    cont += 1

print('Você PERDEU!')
print(f'Você ganhou um total de {cont} vezes.')
