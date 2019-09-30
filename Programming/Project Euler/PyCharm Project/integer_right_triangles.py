from eulerlib import *


"""
A Pythagorean Triplet (a, b, c) can be generated with:
  a = v^2 - u^2
  b = 2uv
  c = u^2 + v^2
where v > u, v and u are not both odd, and gcd(v,u) = 1.

Let a + b + c = P, then P = 2v^2 + 2uv. This gives us a formula
to generate the perimeter P of a primitive Pythagorean Triplet.

We still need to calculate all the multiples of that triplet but
because m(a + b + c) = mP, we can simply multiply P by a multiple
of m, where m >= 1 and mP <= 1000.

Then count all the solutions mP that we found, and return the one
that gave us the most solutions.
"""


def integer_right_triangles(n):
    solutions = [0] * (n + 1)
    v = 2
    u = 1
    p = 12  # [3, 4, 5] has perimeter 12
    while u**2 <= n:
        if p <= n and not (is_odd(v) and is_odd(u)) and gcd(u, v) == 1:
            # u, v combination is a primitive triplet
            m = 1
            q = p
            # find all multiples and increment solutions
            while q <= n:
                solutions[q] += 1
                m += 1
                q = m * p
        u += 1
        if u >= v:
            v += 1
            u = 1
        p = 2*v**2 + 2*u*v  # calculate perimeter

    res = solutions.index(max(solutions))
    print('There are {} solutions for P={}'.format(solutions[res], res))
    return res


def integer_right_triangles_lcd(n):
    lcm_of_p = 12
    for a, b, c in primitive_pythagorean_triplet_generator():
        print('({}, {}, {})'.format(a, b, c))
        if lcm_of_p > n:
            return ans
        ans = lcm_of_p
        lcm_of_p = lcm(lcm_of_p, a + b + c)


time_it(integer_right_triangles, [1000])
time_it(integer_right_triangles_lcd, [1000])
