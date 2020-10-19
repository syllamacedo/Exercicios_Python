print('=' * 30)
print('     10 TERMOS DE UMA PA')
print('=' * 30)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

print(termo, ' -> ', end=' ')
for n in range(0, 9):
    termo = termo + razao
    print(termo, ' -> ', end=' ')
print('ACABOU')
