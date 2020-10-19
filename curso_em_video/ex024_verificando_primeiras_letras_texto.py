# o script vai verificar se o nome da cidade começa com "Santo"

cid = str(input('Em que cidade você nasceu: ')).strip()
print(cid[:5].upper() == 'SANTO')
