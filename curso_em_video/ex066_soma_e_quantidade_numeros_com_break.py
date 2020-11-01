# o script recebe como entrada uma quantidade x de números
# retorna a soma e quantidade de numeros recebidos

cont = soma = 0

while True:
    num = int(input('Digite um número (0 para parar): '))

    if num == 0:
        break

    soma += num
    cont += 1

print(f'\nA quantidade de números digitados foi {cont} e a soma total deles equivale a {soma}.')
