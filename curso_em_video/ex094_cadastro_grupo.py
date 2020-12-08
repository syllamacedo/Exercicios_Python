# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

dados = dict()
dadosfinal = []
media = 0

while True:
    dados['nome'] = str(input('Nome: ')).upper()

    while True:
        dados['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]

        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor digite M ou F.')

    dados['idade'] = int(input('Idade: '))
    dadosfinal.append(dados.copy())
    media = (media + dados['idade']) / len(dadosfinal)

    while True:
        resp = str(input('Deseja continuar? [S/N] ')).upper()[0]

        if resp in 'SN':
            break

        print('ERRO! Por favor digite S ou N.')

    if resp == 'N':
        break
    print()

print('-='*30)
print(f'- O grupo tem {len(dadosfinal)} pessoas\n'
      f'- A média de idade é de {media:.1f}\n'
      f'- As mulheres cadastradas foram: ', end='')

for n in dadosfinal:
    if n['sexo'] == 'F':
        print(f'{n["nome"]};', end=' ')

print(f'\n- Lista das pessoas que estão acima da média:\n')

for n in dadosfinal:
   if n['idade'] > media:
       print(f'Nome = {n["nome"]}; Sexo = {n["idade"]}; Idade = {n["idade"]};')

print()
print('<< ENCERRADO >>')
