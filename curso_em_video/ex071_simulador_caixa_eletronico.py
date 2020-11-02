# o script simula um caixa eletronico onde recebe como entrada o valor do saque
# vai retornar com o total de notas necessarias para realizar o saque
#
# coloquei variaveis para o valor das notas, assim o programa pode ser adaptado mais facilmente
# a qualquer nota que desejarmos

print('=' * 30)
print('{:^30}'.format('BANCO COMUM'))
print('=' * 30)

nota1 = 50
nota2 = 20
nota3 = 10
nota4 = 1

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
