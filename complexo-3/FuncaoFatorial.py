def fatorial(n, show=False):
    """
    => Calcula o fatorial de uma numero.
    :param n: o numero a ser calculado
    :param show: (opcional) mostrar ou não a conta.
    :return: o valor do fatorial de um numero
    Da um help para Funciona
    """
    f = 1
    for c in range(n,0,-1):
        if show:
            print(c,end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

#programa principal
print(fatorial(5,show=True))
print(fatorial(3,show=False))
print(fatorial(5))
help(fatorial)