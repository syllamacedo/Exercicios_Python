maisvelho = ''
media = mulhermenor20 = homemvelho = 0

print('-=' * 20)
for n in range(1, 5):
    print('Informações sobre o {}o indivíduo:'.format(n))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    media += idade
    sexo = str(input('Sexo: [M] ou [F} - ').upper())
    print('-=' * 20)
    if sexo == 'F':
        if idade < 20:
            mulhermenor20 += 1
    else:
        if n == 1:
            homemvelho = idade
            maisvelho = nome
        elif idade >= homemvelho:
            homemvelho = idade
            maisvelho = nome

print('A média de idade do grupo é de {:.1f} anos.'.format(media/2))
print('O homem mais velho do grupo é o {} com {} anos.'.format(maisvelho, homemvelho))
print('Temos {} mulheres no grupo com menos de 20 anos.'.format(mulhermenor20))
