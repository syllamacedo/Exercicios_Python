# o script recebe como entrada o ano de nascimento de 7 pessoas
# no final retorna quantos são maiores e menores de 21

from datetime import date

atual = date.today().year
menor = maior = 0
maioridade = 21

for n in range(1, 8):
    ano = int(input('Em que ano a {}a pessoa nasceu (YYYY): '.format(n)))
    if atual - ano < maioridade:
        menor += 1
    else:
        maior += 1

print('\nAo todo tivemos {} pessoas maiores de idade.\n
        'E tivemos {} pessoas menores de idade.'.format(maior, menor))
