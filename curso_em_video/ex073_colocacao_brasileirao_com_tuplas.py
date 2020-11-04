times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR',
         'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza',
         'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense',
         'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print(f'{" BRASILEIRAO 2019 ":=^50}')
print('CINCO PRIMEIROS COLOCADOS:')
print('-=' * 25)

n = 0
while n < 5:
    print(f'{n + 1}.{times[n].upper()}')
    n += 1

    if n == 5:
        print('-=' * 25)
        print('ZONA DE REBAIXAMENTO')
        n = 16
        while n < 20:
            print(f'{n + 1}.{times[n].upper()}')
            n += 1

print('-=' * 25)
print('TIMES EM ORDEM ALFABÉTICA')
print('-=' * 25)

for t in sorted(times):
    print(t)

print('-=' * 25)
print(f'O time da Chapecoense terminou em {times.index("Chapecoense")+1}o lugar.')
