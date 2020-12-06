# Exercício Python 090: Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
#
# media >= 7 - aprovado
# media >= 5 e < 7 - recuperação
# media < 7 - reprovado

aluno = {'Nome': str(input('Nome: '))}
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))

if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'

print('-='*25)

for v, k in aluno.items():
    print(f'{v}: {k}')
