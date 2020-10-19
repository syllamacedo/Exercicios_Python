valor = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
ano = int(input('Quantos anos de financiamento: '))
prestacao = valor / (ano * 12)
minimo = (salario * 30) / 100

print('Para pagar uma casa de R$ {} em {} anos a prestação será de R$ {:.2f}.\n'.format(valor, ano, prestacao))
if prestacao <= minimo:
    print('Empréstimo APROVADO!')
else:
    print('Empréstico NEGADO!')
