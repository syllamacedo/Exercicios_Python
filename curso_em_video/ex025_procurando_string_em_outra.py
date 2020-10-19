# o script vai verificar se tem Silva no nome

n = str(input('Qual é o seu nome completo: ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in n.lower()))
