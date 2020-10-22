from math import ceil

area = float(input("Qual o tamanho da área a ser pintada? Coloque o valor em metros quadrados: "))
litros = ceil(area / 6)  # 1 litro de tinta pinta 6 metros quadrados
totlitros = litros
lata = 18
galao = 3.6
totlata = totgalao = 0

solata = ceil(totlitros / 18)  # situação 1
sogalao = ceil(totlitros / 3.6)  # situação 2

while True:  # situação 3
    if totlitros >= lata:
        totlitros -= lata
        totlata += 1
    elif totlitros == 0:
        break
    else:
        if totlitros >= galao:
            totlitros -= galao
            totgalao += 1
        else:
            totgalao += 1
            break

valorlata = 80  # 1 lata custa 80 reais
valorgalao = 25  # 1 galão custa 25 reais

print("-=" * 30)
print(f"Para pintar uma área de {area} m2, serão necessários {litros} litros de tinta."
      f"\nSabendo-se que 1 lata possui {lata} litros e 1 galão {galao} litros, temos os cenários:"
      f"\n--> Situação 1:"
      f"\n  comprando apenas latas, serão necessários {solata} latas e vai custar R$ {solata * valorlata}."
      f"\n--> Situação 2:"
      f"\n  comprando apenas galões, serão necessários {sogalao} galões e vai custar R$ {sogalao * valorgalao}."
      f"\n--> Situação 3:"
      f"\n  comprando mesclado, serão necessários {totlata} latas e {totgalao} galões, ao custo de"
      f"R$ {(totlata * valorlata) + (totgalao * valorgalao)}.")
