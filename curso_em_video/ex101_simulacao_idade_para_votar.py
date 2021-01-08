# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
# o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem
# voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano):
    from datetime import datetime

    idade = datetime.now().year - ano

    if idade < 16:
        resp = 'NÃO VOTA'
    elif (16 <= idade < 18) or idade > 70:
        resp = 'VOTO OPCIONAL'
    else:
        resp = 'VOTO OBRIGATÓRIO'

    return f'Com {idade} anos: {resp}'


print('--'*20)
nasc = int(input('Digite seu ano de nascimento: '))
print(voto(nasc))
