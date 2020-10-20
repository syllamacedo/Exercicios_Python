aluno = {'Nome': str(input('Nome: '))}
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'

print('-='*25)
for v, k in aluno.items():
    print(f'{v} é igual a {k}')
