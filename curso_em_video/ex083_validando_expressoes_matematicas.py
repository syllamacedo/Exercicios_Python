# o programa vai analisar uma expressao matematica recebida
# vai realizar uma validacao com base na quantidade de parenteses abertos e fechados
# se a expressao tiver a mesma quantidade de '(' e ')' sera considerada como valida

exp = str(input('Digite a expressão: '))

if exp.count('(') == exp.count(')'):
    print('Sua expressão é válida.')
else:
    print('Sua expressão não é válida.')
