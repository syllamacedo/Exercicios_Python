def voto(idade):
    from datetime import datetime
    idade = datetime.now().year - idade
    if idade < 16:
        resp = 'NÃO VOTA'
    elif (16 <= idade < 18) or idade > 70:
        resp = 'VOTO OPCIONAL'
    else:
        resp = 'VOTO OBRIGATÓRIO'
    return f'Com {idade} anos: {resp}'


print('--'*20)
anonasc = int(input('Digite seu ano de nascimento: '))
print(voto(anonasc))
