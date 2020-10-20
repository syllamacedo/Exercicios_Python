maioridade = homem = mulhervinte = cont = 0

while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = escolha = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        maioridade += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulhervinte += 1
    print('-' * 20)
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    cont += 1
    if escolha == 'N':
        break

print(f"{' FIM DO PROGRAMA ':=^41}")
print('Foram cadastradas {} pessoas.\n'
      'Total de pessoas com mais de 18 anos: {}.\n'
      'Total de homens: {}.\n'
      'Total de mulheres com menos de 20 anos: {}.'.format(cont, maioridade, homem, mulhervinte))
