# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print('GERADOR DE PA')
print('-=' * 10)

num = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

print('-=' * 10)

cont = 1
total = 0
mais = 10
print()

while mais != 0:
    total += mais

    while cont <= total:
        print('{} -> '.format(num), end='')
        num += razao
        cont += 1
    print('PAUSA\n')
    
    mais = int(input('Quantos termos dessa PA você quer ver mais (0 para sair): '))

print('\nProgressão finalizada com {} termos mostrados.'.format(total))
