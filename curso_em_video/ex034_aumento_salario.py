# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual o valor do seu salário: R$ '))
salario_base = 1250
aumento_min = 15
aumento_max = 10

if salario > salario_base:
    novo_salario = salario + ((salario * aumento_max) / 100)
    print('Você terá um aumento de {}% e seu salário agora será R$ {:.2f}.'.format(aumento_max, novo_salario))
else:
    novo_salario = salario + ((salario * aumento_min) / 100)
    print('Você terá um aumento de {}% e seu salário agora será R$ {:.2f}.'.format(aumento_min, novo_salario))
