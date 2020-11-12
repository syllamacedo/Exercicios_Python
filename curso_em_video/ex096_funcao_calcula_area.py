def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {a}m2.')


print(' Controle de Terrenos')
print('-'*20)

largura = float(input('LARGURA (m): '))
comprimento = float(input('CCOMPRIMENTO (m): '))

area(largura, comprimento)
