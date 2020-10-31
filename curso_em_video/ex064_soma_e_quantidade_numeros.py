# o script recebe como entrada uma quantidade x de números
# retorna a soma e quantidade de numeros recebidos

num = cont = -1
soma = 1

while num != 0:
    soma += num
    num = int(input('Digite um número inteiro [0 para parar]: '))
    cont += 1

print('\nA soma dos números digitados é igual a {}.\n'
      'A quantidade de números digitados foi {}.'.format(soma, cont))
