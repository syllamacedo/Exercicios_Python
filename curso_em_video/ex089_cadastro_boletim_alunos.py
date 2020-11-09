# o script vai receber o nome e 2 notas de n alunos
# apos termino do cadastro o programa vai retornar a quantidade de alunos, nome e media de cada
# no final o usuario vai poder selecionar qual aluno deseja ver as notas

from time import sleep

print('-=' * 20)
print(f'{"CADASTRO DE NOTAS":^40}')
print('-=' * 20)

ficha = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('1a Nota: '))
    nota2 = float(input('2a Nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = ' '

    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]: ')).strip().upper()

    print()
    if resp == 'N':
        break

print('-' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)

for i, a in enumerate(ficha):
    print(f'{(i+1):<4}{a[0]:<10}{a[2]:>8.1f}')

print('-' * 30)
while True:
    mostra = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    if mostra != 999:
        mostra -= 1
        if mostra in range(len(ficha)):
            print(f"Notas de {ficha[mostra][0]} são {ficha[mostra][1]}")
            print('-' * 30)

    if mostra == 999:
        print('-' * 30)
        print('FINALIZANDO...')
        sleep(1)
        break

print('<<< VOLTE SEMPRE >>>')
