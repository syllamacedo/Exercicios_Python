exp = str(input('Digite a expressão: '))
if exp.count('(') == exp.count(')'):
    print('Sua expressão é valida.')
else:
    print('Sua expressão não é valida.')
