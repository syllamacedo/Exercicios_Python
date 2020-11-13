# o script vai receber os dados de um funcionario
# se o usuario passar numero de carteira de trabalho, serao pedidos mais dados
# ao final o programa vai mostrar os dados do funcionario
# se tiver carteira de trabalho, sera indicado se já é aposentado ou quanto tempo falta
# o tempo de contribuicao considerado foi de 35 anos

from datetime import datetime

dados = {'Nome': str(input('Nome: '))}
ano = int(input('Ano de Nascimento [AAAA]: '))
dados['Idade'] = datetime.now().year - ano
dados['CTPS'] = int(input('Carteira de Trabalho [0 não tem]: '))

if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação [AAAA]: '))
    dados['Salário'] = float(input('Salário: R$ '))
    tempo_contribuicao = 35
    contribuicao = tempo_contribuicao - (datetime.now().year - dados['Contratação'])

    if contribuicao <= 0:
        dados['Aposentadoria'] = 'Já é aposentado(a)'
    else:
        dados['Aposentadoria'] = f'com {dados["Idade"] + contribuicao} anos'

if dados['CTPS'] == 0:
    dados['CTPS'] = 'Não possui'

print('-=' * 30)
for k, v in dados.items():
    print(f'{k}: {v}')
