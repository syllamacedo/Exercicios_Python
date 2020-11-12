# o script vai receber os dados de um funcionario
# se o usuario passar numero de carteira de trabalho, serao pedidos mais dados
# ao final o programa vai mostrar os dados do funcionario
# se tiver carteira de trabalho, sera indicado se já é aposentado ou quanto tempo falta

from datetime import datetime

dados = {'Nome': str(input('Nome: '))}
ano = int(input('Ano de Nascimento: '))
dados['Idade'] = datetime.now().year - ano
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$ '))
    contribuicao = 35 - (datetime.now().year - dados['Contratação'])

    if contribuicao <= 0:
        dados['Aposentadoria'] = 'Já é aposentado'
    else:
        dados['Aposentadoria'] = dados['Idade'] + contribuicao

print('-=' * 30)
for k, v in dados.items():
    print(f'{k}: {v}')
