from datetime import date

ano = int(input('Digite o ano de nascimento do seu atleta: '))
atual = date.today().year
idade = atual - ano

if idade <= 9:
    categoria = 'MIRIM'
elif 9 < idade <= 14:
    categoria = 'INFANTIL'
elif 14 < idade <= 19:
    categoria = 'JUNIOR'
elif 19 < idade <= 25:
    categoria = 'SÊNIOR'
elif idade > 25:
    categoria = 'MASTER'

print('\nSeu atleta está com {} anos. Com essa idade, ele vai competir na categoria {}.'.format(idade, categoria))
