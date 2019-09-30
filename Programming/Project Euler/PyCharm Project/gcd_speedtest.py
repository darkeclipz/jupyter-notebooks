from eulerlib import *


def gcd2(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


#  Generalized repunit primes; Of the form (an − 1) / (a − 1) for fixed integer a.
a = 14693679385278593849609206715278070972733319459651094018859396328480215743184089660644531
b = 3546245297457217493590449191748546458005595187661976371
c = 85053461164796801949539541639542805770666392330682673302530819774105141531698707146930307290253537320447270457

x0 = a * b
x1 = b * c


def loop(f, a, b): return [f(a, b) for _ in range(10000)][0]


time_it(loop, [gcd, x0, x1])
time_it(loop, [gcd2, x0, x1])


# gcd is approx ~12.5% faster
