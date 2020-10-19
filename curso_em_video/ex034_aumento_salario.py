# o script lê o salario atual e retorna com o novo valor
# aumento: 15% para salarios até R$1250 e 10% para valores acima

sal = float(input('Qual o valor do seu salário: R$ '))

if sal > 1250:
    print('Você terá um aumento de 10% e seu salário agora será R$ {:.2f}.'.format(sal + (sal * 10) / 100))
else:
    print('Você terá um aumento de 15% e seu salário agora será R$ {:.2f}.'.format(sal + (sal * 15) / 100))
