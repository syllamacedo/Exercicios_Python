# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maior_idade = homem = mulher_vinte = cont = 0

while True:
    print('-=' * 12)
    print('CADASTRE UMA PESSOA')
    print('-=' * 12)

    idade = int(input('Idade: '))
    sexo = escolha = ' '

    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    if idade >= 18:
        maior_idade += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher_vinte += 1

    print()
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]

    cont += 1

    if escolha == 'N':
        break

print(f"{' FIM DO PROGRAMA ':=^41}")
print('Foram cadastradas {} pessoas.\n'
      'Total de pessoas com mais de 18 anos: {}\n'
      'Total de homens: {}\n'
      'Total de mulheres com menos de 20 anos: {}'.format(cont, maior_idade, homem, mulher_vinte))
