num = soma = cont = 0
while num != 999:
    soma += num
    num = int(input('Digite um número [999 para parar]: '))
    cont += 1
print('A soma dos números digitados é igual a {}.\n'
      'A quantidade de números digitados foi {}.'.format(soma, cont - 1))
