def ajuda(comando):
    from time import sleep

    if comando == 'fim':
        print('~~' * 25)
        return 'Até Logo!'
    else:
        sleep(0.5)
        print('~~' * 25)
        print(f'Acessando o manual do comando {comando}')
        print('~~' * 25)
        sleep(0.5)
        return help(comando)


while True:
    print('~~' * 25)
    print('Sistema de ajuda PyHELP')
    print('~~' * 25)

    c = ajuda(input('Função ou biblioteca: ').lower().strip())

    print(c)
    if c == 'Até Logo!':
        break
