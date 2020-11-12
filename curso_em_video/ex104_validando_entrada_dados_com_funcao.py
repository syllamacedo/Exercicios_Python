def leiaint(num):
    while not num.isnumeric():
        print('\033[0;31mERRO! Digite um número válido.\033[m')
        num = (input('Digite um número: '))

    return num


n = leiaint(input('Digite um número: '))
print(f'Você acabou de digitar o número {n}.')
