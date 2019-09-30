from eulerlib import *


def integer_right_triangles(n):
    solutions = [0] * (n + 1)
    v = 2
    u = 1
    p = 12  # [3, 4, 5] has perimeter 12
    while u**2 <= n:
        if p <= 1000 and not is_odd(v) and is_odd(u):
            a = 1
            q = p
            while q <= 1000:
                solutions[q] += 1
                a += 1
                q = a * p
        u += 1
        if u >= v:
            v += 1
            u = 1
        p = 2*v**2 + 2*u*v
    return solutions.index(max(solutions))


time_it(integer_right_triangles, [1000])
