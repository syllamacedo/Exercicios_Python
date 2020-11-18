# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar
# quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('=' * 30)
print('{:^30}'.format('BANCO COMUM'))
print('=' * 30)

nota1, nota2, nota3, nota4 = 50, 20, 10, 1

print(f'Notas disponíveis: {nota1} - {nota2} - {nota3} - {nota4}')

valor = int(input('Qual valor você quer sacar? R$ '))
print()

while True:

    if valor >= nota1:
        total_nota1 = valor // nota1
        print(f'Total de {total_nota1} cédulas de R${nota1}.')
        if valor % nota1 == 0:
            break
    else:
        total_nota1 = 0

    resto = valor - (total_nota1 * nota1)
    total_nota2 = resto // nota2

    if total_nota2 > 0:
        print(f'Total de {total_nota2} cédulas de R${nota2}.')
        if resto % nota2 == 0:
            break

    resto = resto - (total_nota2 * nota2)
    total_nota3 = resto // nota3

    if total_nota3 > 0:
        print(f'Total de {total_nota3} cédulas de R${nota3}.')
        if valor % nota3 == 0:
            break

    resto = valor - ((total_nota1 * nota1) + (total_nota2 * nota2) + (total_nota3 * nota3))
    total_nota4 = resto // nota4
    print(f'Total de {total_nota4} cédulas de R${nota4}.')

    break
