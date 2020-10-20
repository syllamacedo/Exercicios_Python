def fatorial(n, show=False):
    """
    Programa que calcula o fatorial de um número
    :param n: O número a ser calculado
    :param show: se o usuário deseja ou não ver o cálculo feito
    :return: o valor do fatorial
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, True))
print(help(fatorial))
