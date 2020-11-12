from time import sleep


def maior(*num):
    maiornum = 0

    print('-=' * 20)
    print('Analisando os valores passados...')

    for n in num:
        print(f'{n}', end=' ')
        sleep(0.5)
        if n >= maiornum:
            maiornum = n

    print(f'\nForam informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maiornum}.')


maior(6)
maior()  # Passando nenhum valor
maior(2, 9, 4, 5, 7, 1)

# FAZENDO COM LISTA E PEDINDO AO USUARIO QUE PREENCHA OS NÚMEROS:
# Função vai ser a mesma, só vai mudar a variavel "num"

''' 
def maior(lst):
    maior = 0
    print('-=' * 20)
    print('Analisando os valores passados...')
    for n in lst:
        print(f'{n}', end=' ')
        sleep(0.5)
        if n >= maior:
            maior = n
    print(f'\nForam informados {len(lst)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


m = []
while True:
    m.append(int(input('Digite um número: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]? ')).upper()
    if resp == 'N':
        break

maior(m)
'''
