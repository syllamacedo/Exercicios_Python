n = str(input('Digite seu nome completo: ')).strip()

# procurando os nomes baseado nos espaços entre eles:
print('Seu primeiro nome é {}.'.format(n[:n.find(' ')]))
print('Seu último nome é {}.'.format(n[n.rfind(' '):]))

# outra forma de fazer
# procurando utilizando split
nome = n.split()
print('Seu primeiro nome é {}.'.format(nome[0]))
print('Seu último nome é {}.'.format(nome[len(nome)-1]))
