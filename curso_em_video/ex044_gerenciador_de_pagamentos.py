# o script vai receber a entrada de um valor 
# e informar as opções para pagamento do mesmo, pedindo que o usuário escolha dentre uma delas

preco = float(input('Digite o valor do produto: R$ '))
print('''\nFORMAS DE PAGAMENTO
[ 1 ] A vista dinheiro ou cheque - 10% de desconto
[ 2 ] A vista cartão - 5% de desconto
[ 3 ] Parcelado em 2x no cartão
[ 4 ] Parcelado em 3x ou mais vezes - 20% de juros''')
opcao = int(input('\nQual será sua forma de pagamento: '))

if opcao == 1:
    valor = preco - ((preco * 10) / 100)
elif opcao == 2:
    valor = preco - ((preco * 5) / 100)
elif opcao == 3:
    valor = preco
    print('Sua compra será parcelada em 2x de R$ {}, SEM JUROS.'.format(valor/2))
elif opcao == 4:
    valor = preco + ((preco * 20) / 100)
    vezes = int(input('Deseja pagar em quantas parcelas: '))
    parcela = valor / vezes
    print('Sua compra será parcelada em {}x de R$ {:.2f}, COM JUROS.'.format(vezes, parcela))
else:
    valor = preco
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente.')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preco, valor))
