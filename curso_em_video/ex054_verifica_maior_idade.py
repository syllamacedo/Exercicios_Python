# Programa que tem como entrada o ano de nascimento de 7 pessoas
# No final o programa retorna quantos são maiores e menores de 21

from datetime import date

atual = date.today().year
menor = maior = 0

for n in range(1, 8):
    ano = int(input('Em que ano a {}a pessoa nasceu: '.format(n)))
    if atual - ano < 21:
        menor += 1
    else:
        maior += 1

print('Ao todo tivemos {} pessoas maiores de idade.'.format(maior))
print('E também tivemos {} pessoas menores de idade.'.format(menor))
