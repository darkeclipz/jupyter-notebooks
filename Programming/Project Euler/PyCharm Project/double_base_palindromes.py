import eulerlib
import math


def double_base_palindromes():
    palindromes = eulerlib.palindromes(1, 1e6+1)
    result = []
    for p in palindromes:
        p_bin = eulerlib.to_binary_string(p)
        if eulerlib.is_palindrome(p_bin):
            print('{} = {}'.format(p, p_bin))
            result.append(p)
    return sum(result)


eulerlib.time_it(double_base_palindromes)
