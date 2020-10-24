from datetime import date

ano = int(input('Qual seu ano de nascimento: '))
atual = date.today().year
idade = atual - ano

print('\nQuem nasceu em {} tem {} ano(s) em {}.'.format(ano, idade, atual))
if idade < 18:
    falta = 18 - idade
    alistamento = atual + falta
    print('Ainda faltam {} ano(s) para o alistamento.\n'
          'Seu alistamento será em {}.'.format(falta, alistamento))
elif idade == 18:
    print('Você deve se alistar no serviço militar obrigatório.')
elif idade > 18:
    saldo = idade - 18
    alistamento = atual - saldo
    print('Você já deveria ter se alistado há {} ano(s).\n'
          'Seu alistamento foi em {}, se você não se alistou, vá regularizar sua situação.'.format(saldo, alistamento))
