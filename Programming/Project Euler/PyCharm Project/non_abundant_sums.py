import eulerlib


def non_abundant_sums(n):
    sieve = eulerlib.sum_of_proper_divisors_sieve(n + 1)
    checked = {x: False for x in range(1, n + 1)}
    abundant_numbers = [x for x in range(1, n + 1) if sieve[x] > x]
    length = len(abundant_numbers)
    for i in range(length):
        for j in range(i, length):
            s = abundant_numbers[i] + abundant_numbers[j]
            if s <= n:
                checked[s] = True
    return sum([k for k, v in checked.items() if not v])


eulerlib.time_it(non_abundant_sums, args=[28123])  # answer is 4179871
