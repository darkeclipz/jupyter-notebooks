import eulerlib
import math


def pandigital_products():
    res = 0
    memo = []
    bound = 10000
    set_of_1_to_9 = set(range(1, 10))
    for a in range(2, bound):
        log10a = math.log(a, 10)
        inner_exp = 7/2 - log10a
        if not eulerlib.is_unique_string(str(a)):
            continue
        lower_bound_for_b = int(10**inner_exp)
        for b in range(lower_bound_for_b, 10*lower_bound_for_b):
            log10b = math.log(b, 10)
            log10c = log10a + log10b
            log_digits = int(log10a + log10b + log10c)
            if log_digits != 7:
                continue
            c = a * b
            mmi = int(str(a) + str(b) + str(c))
            digits_of_mmi = eulerlib.digits(mmi)
            if c not in memo and set(digits_of_mmi) == set_of_1_to_9:
                print('{} x {} = {}  ({})'.format(a, b, c, mmi))
                res += c
                memo.append(c)
    return res


eulerlib.time_it(pandigital_products)
