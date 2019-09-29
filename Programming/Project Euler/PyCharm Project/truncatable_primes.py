from eulerlib import *


def is_truncatable_prime(p, sieve):
    p_str = str(p)
    if len(p_str) <= 1:
        return False
    if not sieve[p]:
        return False
    for i in range(1, len(p_str)):
        if not sieve[int(p_str[i:])]:
            return False
        if not sieve[int(p_str[:i])]:
            return False
    return True


def truncatable_primes():
    sieve = prime_sieve(1_000_000)
    primes = sieve_to_list(sieve)
    result = []
    for p in primes:
        if is_truncatable_prime(p, sieve):
            print(p)
            result.append(p)
            if len(result) == 11:
                break
    print('Number of primes: {}'.format(len(result)))
    return sum(result)


time_it(truncatable_primes)
