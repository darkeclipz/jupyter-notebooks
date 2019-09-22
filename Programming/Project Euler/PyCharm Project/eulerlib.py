import math
import time


def time_it(f, args=None):
    t0 = time.time()
    print('Running...')
    result = f(*args)
    print('Solution is {}.'.format(result))
    t1 = time.time()
    print('Executed in {} seconds.'.format(round(t1 - t0, 4)))


def distinct(x):
    """
    Returns a list of unique elements.
    :param x: List of elements.
    :return: List of unique elements.
    """
    return list(set(x))


def divisors(x):
    """
    Returns all the divisors for a number x, including x.
    e.g divisors(1001) = [1, 7, 11, 13, 77, 91, 143, 1001]
    :param x: number >= 1.
    :return: the divisors including 1 and x.
    """
    x = abs(x)
    result = []
    upper_bound = int(math.sqrt(x))
    for i in range(1, upper_bound + 1):
        if x % i == 0:
            if x / i == i:
                result.append(i)
            else:
                result.append(i)
                result.append(x//i)
    return sorted(distinct(result))


def sum_of_proper_divisors_sieve(n):
    sieve = [1] * (n + 1)
    for i in range(2, n // 2 + 1):
        for j in range(i + i, n, i):
            sieve[j] += i
    return sieve


def proper_divisors(x):
    """
    Returns all the proper divisors for a number x, excluding x.
    e.g divisors(1001) = [1, 7, 11, 13, 77, 91, 143]
    :param x: number >= 1.
    :return: the divisors excluding itself.
    """
    return divisors(x)[:-1]


def restricted_divisors(x):
    """
    Returns all the restricted divisors for a number x, excluding 1 and x.
    e.g divisors(1001) = [7, 11, 13, 77, 91, 143]
    :param x: number >= 1.
    :return: the divisors excluding 1 and itself.
    """
    return divisors(x)[1:-1]


def is_perfect_number(x):
    """
    Test if a number is a perfect number. A number is perfect
    if the sum of the proper divisors is equal to itself.
    :param x: number to test.
    :return: True if it is a perfect number.
    """
    return sum(proper_divisors(x)) == x


def is_abundant_number(x):
    """
    Test if a number is an abundant number. A number is abundant
    if the sum of the proper divisors is greater than the number
    itself.
    :param x: number to test.
    :return: True if it is an abundant number.
    """
    return sum(proper_divisors(x)) > x


def is_deficient_number(x):
    """
    Test if a number is a deficient number. A number is deficient
    if the sum of the proper divisors is less than the number
    itself.
    :param x: number to test.
    :return: True if it is a deficient number.
    """
    return sum(proper_divisors(x)) < x


def is_fibonacci_number(x):
    """
    Test if x is a Fibonacci number.
    :param x: Number to test.
    :return: True if it is a Fibonacci number.
    """
    a = math.sqrt(5 * x ** 2 + 4)
    b = math.sqrt(5 * x ** 2 - 4)
    return a.is_integer() or b.is_integer()


def fibonacci_n(n):
    """
    Calculate the nth Fibonacci number (Fn).
    :param n: which number to calculate.
    :return: The nth Fibonacci number.
    """
    sqrt5 = math.sqrt(5)
    phi = (1 + sqrt5) / 2
    psi = (1 - sqrt5) / 2
    return (phi**n - psi**n) // sqrt5


def fibonacci_n_inv(x):
    """
    Calculate the n for Fn for a Fibonacci number.
    :param x: Fibonacci number.
    :return: The position of the Fibonacci number (Fn)
    """
    sqrt5 = math.sqrt(5)
    phi = (1 + sqrt5) / 2
    rad = 5 * x**2
    p = math.sqrt(5*x**2 + 4)
    n = math.log((x * sqrt5 + math.sqrt(rad + 4)) / 2, phi) \
        if p.is_integer() \
        else math.log((x * sqrt5 + math.sqrt(rad - 4)) / 2, phi)
    return round(n)


def gcd(a, b):
    """
    Determines the greatest common divisor for a and b
    with the Euclidean Algorithm.
    :param a: First number.
    :param b: Second number.
    :return: Greatest common divisor for a and b.
    """
    a = abs(a)
    b = abs(b)
    if a == b:
        return a
    if b > a:
        a, b = b, a
    q = a // b
    r = a - b * q
    while r != 0:
        a = b
        b = r
        q = a // b
        r = a - b * q
    return b
