from datetime import date

ano = int(input('Digite o ano de nascimento do seu atleta: '))
atual = date.today().year
idade = atual - ano
print('Seu atleta está com {} anos. Com essa idade, ele vai competir na categoria:'.format(idade))

if idade <= 9:
    print('MIRIM')
elif 9 < idade <= 14:
    print('INFANTIL')
elif 14 < idade <= 19:
    print('JUNIOR')
elif 19 < idade <= 25:
    print('SÊNIOR')
elif idade > 25:
    print('MASTER')
