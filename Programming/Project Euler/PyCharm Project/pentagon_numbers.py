import eulerlib
import math
import quadratic


def pentagon_numbers():
    """
    This is absurdly slow, fix it ....
    :return:
    """
    min_d = math.inf
    n = 10000
    lt = [eulerlib.pentagonal_number(i) for i in range(0, n + 1)]
    for j in range(1, n):
        for k in range(1, j + 1):
            px = lt[j]
            py = lt[k]
            if px == py:
                continue
            d = abs(px - py)
            if eulerlib.is_pentagonal_number(px + py) \
               and eulerlib.is_pentagonal_number(d) \
               and d < min_d:
                min_d = d
    return min_d


def pentagon_numbers2():
    for n in range(1, 1000):
        for i in range(1, n):
            c = (3 * i**2 + 6 * n * i - 2 * n - i) * 2
            _, x2 = quadratic.solve(3, -1, -2 * c)
            if eulerlib.is_number(x2) and x2.is_integer():
                print(c, x2)
                # check if the sum is pentagonal too
                # ...


# Calculate difference directly P(k) = P(n + i) - P(n), and check if P(k) is pentagonal.
# Then check if P(n + i) + P(n) is pentagonal too. That's it, in theory...


eulerlib.time_it(pentagon_numbers2)
#eulerlib.time_it(pentagon_numbers)

