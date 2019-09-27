import eulerlib


def consecutive_prime_sum():
    sieve = eulerlib.prime_sieve(1000000)  # takes ~0.5 sec to load
    primes = [i for i, v in enumerate(sieve) if v]
    max_s = 0
    max_len = 0
    max_i = 0
    # 551 = number of primes needed when the sum >1 M
    # 551 = len([i for i, v in enumerate(eulerlib.prime_sieve(1000000//50//5)) if v])
    number_of_primes_till_sum_1m = 551
    for i in range(0, number_of_primes_till_sum_1m):
        for k in range(i, number_of_primes_till_sum_1m, 2):
            if k * primes[i] > 1000000:
                break
            s = sum(primes[i:k+1])
            if s > 1000000:
                break
            if sieve[s] and k - i > max_len:
                max_s = s
                max_len = k - i
                max_i = i

    print('Number of terms: {}'.format(max_len))
    print('Sum starts at n: {}'.format(max_i))
    print('Sum starts at P: {}'.format(primes[max_i]))
    return max_s


eulerlib.time_it(consecutive_prime_sum)
