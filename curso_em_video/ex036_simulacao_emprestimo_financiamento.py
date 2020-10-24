# o script vai simular um pedido se empréstimo com base nos dados de entrada
# para o empréstimo ser aprovado, o valor de cada prestação deverá ser menor ou igual a 30% do salário

valor = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
ano = int(input('Quantos anos de financiamento: '))
prestacao = valor / (ano * 12)
minimo = (salario * 30) / 100

print('Para pagar uma casa de R$ {} em {} anos a prestação será de R$ {:.2f}.\n'.format(valor, ano, prestacao))
if prestacao <= minimo:
    print('Empréstimo APROVADO!')
else:
    print('Empréstico NEGADO! \nPara conseguir o empréstimo a prestação deve ser menor que ou igual a R$ {}'.format(minimo))
