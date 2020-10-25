# o script pede para o usuário digitar 6 valores
# ao final será dito quantos número pares foram digitados e a soma dos mesmos

soma = cont = 0
for n in range(1, 7):
    par = int(input('Digite o {}o valor inteiro: '.format(n)))
    if par % 2 == 0:
        soma += par
        cont += 1
print('Você informou {} número PARES e a soma deles é igual a {}.'.format(cont, soma))
