# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
# ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt(‘Digite um n: ‘)

def leiaint(num):
    while not num.isnumeric():
        print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        num = (input('Digite um número inteiro: '))

    return num


n = leiaint(input('Digite um número inteiro: '))
print(f'Você acabou de digitar o número {n}.')
