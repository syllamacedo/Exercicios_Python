print('O Hipermercado Veggie está com uma promoção que é imperdível. Confira:'
      '\n'
      '\n                      Até 5 Kg               Acima de 5 Kg'
      '\n[0] Soja           R$ 4,90 por Kg          R$ 5,80 por Kg'
      '\n[1] Tofu           R$ 5,90 por Kg          R$ 6,80 por Kg'
      '\n[2] Seitan         R$ 6,90 por Kg          R$ 7,80 por Kg')
print('=-' * 30)
while True:
    n = int(input('Digite o número relativo ao item que deseja comprar: '))
    if n in range(0, 3):
        k = float(input('Quantos kg deseja comprar: '))
        break

ate5 = [('Soja','4.9'), ('Tofu', '5.9'), ('Seitan', '6.9')]
acima5 = [('Soja','5.8'), ('Tofu', '6.8'), ('Seitan', '7.8')]

if k == 0:
    print('Você não comprou uma quantidade mínima.')
elif 0 < k <= 5:
    valor = float(ate5[n][1]) * k
else:
    valor = float(acima5[n][1]) * k

while True:
    cartao = str(input('Vai pagar com o cartão VeggieMais? [S/N] ')).upper()
    if cartao in 'SN':
        if cartao == 'S':
            pagamento = 'Cartão VeggieMais'
            desconto = (valor * 5) / 100
        else:
            desconto = 0
            pagamento = 'não é cliente Cartão VeggieMais'
        break

total = valor - desconto

print('=-' * 30)
print('         Cupom Fiscal'
      '\n-------------------------------'
      f'\nProduto: {ate5[n][0]}'
      f'\nQuantidade: {k} kg'
      f'\nTotal: R$ {valor:.2f}'
      f'\nForma de Pagamento: {pagamento}'
      f'\nDesconto: R$ {desconto:.2f}'
      f'\nValor a Pagar: R$ {total:.2f}')
