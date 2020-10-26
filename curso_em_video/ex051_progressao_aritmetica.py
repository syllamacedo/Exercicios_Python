print('=' * 30)
print('     10 TERMOS DE UMA PA')
print('=' * 30)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

print(termo, ' -> ', end=' ')

# o range será 9 pois o usuário já passa o 1o termo, assim fazem 10 termos ao total
for n in range(9):
    termo = termo + razao
    print(termo, ' -> ', end=' ')
print('ACABOU')
