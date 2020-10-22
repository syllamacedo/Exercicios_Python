# o script lê o salario atual e retorna com o novo valor
# aumento: 15% para salarios até R$1250 e 10% para valores acima

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
