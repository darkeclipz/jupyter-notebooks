import eulerlib


def circular_primes():
    sieve = eulerlib.prime_sieve(1000000)
    primes = [i for i, v in enumerate(sieve) if v]
    result = 0
    for p in primes:
        is_circular_prime = True
        prime_c = eulerlib.digits(p)
        for _ in range(len(prime_c) - 1):
            prime_c = eulerlib.shift(prime_c)
            if not sieve[eulerlib.digits_to_int(prime_c)]:
                is_circular_prime = False
                break
        if is_circular_prime:
            print(p)
            result += 1
    return result


eulerlib.time_it(circular_primes)
