sexo = str(input('Informe o seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Informe o seu sexo: [M/F] ')).strip().upper()[0]
if sexo == 'F':
    sexo = 'Feminino'
elif sexo == 'M':
    sexo = 'Masculino'
print('Você é do sexo {}.'.format(sexo))
