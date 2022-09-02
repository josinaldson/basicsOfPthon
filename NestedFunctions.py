"""def exp(N):
    def elev(X):
        print(X**N)
    return elev

f = exp(3)
f(3)
"""

def lisa():
    start = 0
    lista = []
    def incre(item):
        nonlocal lista, start
        lista.append(item)
        start += 1
        print(item,start)
    return incre
compras = lisa()

compras('presunto')
compras('Apresuntado')


