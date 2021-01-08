# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n, show=False):
    """
    Programa que calcula o fatorial de um número
    :param n: O número a ser calculado
    :param show: se o usuário deseja ou não ver o cálculo feito
    :return: o valor do fatorial
    """
    f = 1

    print('-' * 30)
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c

    return f


# Programa Principal
print(fatorial(5, True))  # pedindo para mostrar o cálculo
print(fatorial(6))  # sem mostrar o cálculo
