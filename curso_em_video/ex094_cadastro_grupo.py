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

print('-='*30)
print(f'- O grupo tem {len(dadosfinal)} pessoas.\n'
      f'- A média de idade é de {media:5.1f}.\n'
      f'- As mulheres cadastradas foram: ', end='')
for n in dadosfinal:
    if n['sexo'] == 'F':
        print(f'{n["nome"]};', end=' ')

print(f'\n- Lista das pessoas que estão acima da média: ')
for n in dadosfinal:
    if n['idade'] > media:
        for k, v in n.items():
            print(f'{k} = {v};', end=' ')
# FORMA PARA FICAR MAIS BONITA A FORMATAÇÃO
# for n in dadosfinal:
#    if n['idade'] > media:
#        print(f'\nNome = {n["nome"]}; Sexo = {n["idade"]}; Idade = {n["idade"]};')
print('\n<< ENCERRADO >>')
