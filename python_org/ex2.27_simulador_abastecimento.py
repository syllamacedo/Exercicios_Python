gasolina = 2.50
alcool = 1.90

while True:
    tipo = str(input('Deseja abastecer com Álcool ou Gasolina? [A/G] ')).upper()
    if tipo in 'AG':
        break

qnt = int(input('Quantidade de litros: '))

if tipo == 'A':
    if qnt <= 20:
        total = (qnt * alcool)
        desconto = (total * 3) / 100
    else:
        total = (qnt * alcool)
        desconto = (total * 5) / 100
elif tipo == 'G':
    if qnt <= 20:
        total = (qnt * gasolina)
        desconto = (total * 4) / 100
    else:
        total = (qnt * gasolina)
        desconto = (total * 6) / 100

print(f'Desconto recebido: R$ {desconto:.2f}'
      f'\nTotal: R$ {total - desconto:.2f}')