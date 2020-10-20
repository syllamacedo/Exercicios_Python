from datetime import datetime
dados = {'Nome': str(input('Nome: '))}

ano = int(input
          ('Ano de Nascimento: '))
dados['Idade'] = datetime.now().year - ano
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$ '))
    contri = 35 - (datetime.now().year - dados['Contratação'])
    if contri < 0:
        dados['Aposentadoria'] = 'Já é aposentado'
    else:
        dados['Aposentadoria'] = dados['Idade'] + contri
print('-=' * 30)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
