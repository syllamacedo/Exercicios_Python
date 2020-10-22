peso = float(input("Qual peso total dos peixes que está trazendo? Kg "))
excesso = peso - 50
multa = excesso * 4
if excesso <= 0:
    multa = 0
    print(f'Com o peso total de {peso}kg de peixes, você não está ultrapassando o limite de 50kg e não será multado.')
else:
    print(f'Com o peso total de {peso}kg de peixes, você ultrapassou o limite em {excesso:.1f}'
          f'kg e terá de pagar uma multa de R${multa:.2f}')
