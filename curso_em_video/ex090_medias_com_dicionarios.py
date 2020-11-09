# o script vai receber como entrada o nome e media de um aluno
# ao final vai retornar o nome, a media e a situacao do aluno
# media >= 7 esta aprovado
# media < 7 esta reprovado

aluno = {'Nome': str(input('Nome: '))}
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))

if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'

print('-='*25)

for v, k in aluno.items():
    print(f'{v}: {k}')
