# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.

from time import sleep

def ajuda(comando):
    sleep(0.5)
    print('~~' * 25)
    print(f'Acessando o manual do comando {comando}')
    print('~~' * 25)
    sleep(0.5)
    return help(comando)


# Programa Principal
while True:
    print('~~' * 25)
    print('Sistema de ajuda PyHELP')
    print('~~' * 25)

    comando = str(input('Função ou biblioteca: ').lower().strip())
    if comando == 'fim':
        sleep(0.3)
        print('Até Logo!')
        break
    else:
        ajuda(comando)
