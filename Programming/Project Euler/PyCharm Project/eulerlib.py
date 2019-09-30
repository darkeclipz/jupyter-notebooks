import math
import time
import quadratic


def time_it(f, args=None):
    t0 = time.time()
    print('--- Timed execution for {} ----------------'.format(f.__name__))
    print('Running...')
    result = f(*args) if args is not None else f()
    print('Solution is {}'.format(result))
    t1 = time.time()
    print('Executed in {} seconds'.format(round(t1 - t0, 6)))


def distinct(x):
    """
    Returns a list of unique elements.
    :param x: List of elements.
    :return: List of unique elements.
    """
    return list(set(x))


def is_number(n):
    return isinstance(n, (int, float))


def is_unique_string(s):
    """
    Determines if a given string only consists of unique
    characters.
    :param s: The string to test.
    :return: True if the string only contains unique characters.
    """
    return len(s) == len(set(s))


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
    """
    Generates an array with the sum of the divisors
    for that index of the array. To find the sum of
    divisors for 12: sieve[12].
    :param n: Upper limit of numbers.
    :return: List with sum of divisors.
    """
    sieve = [1] * (n + 1)
    for i in range(2, n // 2 + 1):
        for j in range(i + i, n, i):
            sieve[j] += i
    return sieve


def prime_sieve(n):
    """
    Generates an array which determines if the index
    of the array is a prime number. To see if 997 is
    a prime number: sieve[997] == True.
    :param n: Upper limit of numbers.
    :return: List with boolean values.
    """
    upper_bound = int(math.sqrt(n))
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(upper_bound + 1):
        if not primes[i]:
            continue
        for j in range(2, n // i + 1):
            if i*j < n:
                primes[i*j] = False
    return primes


def sieve_to_list(sieve):
    """
    Returns the sieve as a list where the index is the number
    where it was True.
    :param sieve:
    :return:
    """
    return [i for i, v in enumerate(sieve) if v]


def triangle_number(n):
    """
    Calculate the nth triangle number.
    :param n: Fn
    :return: Triangle number for n.
    """
    return n * (n + 1) // 2


def is_triangle_number(n):
    """
    Tests if a number is a triangle number. Solved with the
    inverse of n(n+1)/2, and testing if that solution
    is integer.
    :param n: Number to test.
    :return: True if it is a triangle number.
    """
    _, x = quadratic.solve(1, 1, -2*n)
    return is_number(x) and x.is_integer()


def triangle_number_sieve(n):
    """
    Generates a sieve which can be used to tell if a number
    is a triangle number.
    :param n: Up to which n.
    :return: Sieve with boolean values, sieve[3] = True.
    """
    triangle_numbers = [False] * (n + 1)
    tn = i = 1
    while tn < n:
        triangle_numbers[triangle_number(i)] = True
        i += 1
        tn = triangle_number(i)
    return triangle_numbers


def hexagonal_number(n):
    """
    Calculate the nth hexagonal number.
    :param n: Hn
    :return: Hexagonal number
    """
    return n * (2 * n - 1)


def is_hexagonal_number(n):
    """
    Determines if n is a hexagonal number.
    :param n: Hn
    :return: Hexagonal number
    """
    _, x = quadratic.solve(2, -1, -n)
    return is_number(x) and x.is_integer()


def pentagonal_number(n):
    return n * (3 * n - 1) / 2


def is_pentagonal_number(n):
    """
    Determines if n is a pentagonal number.
    :param n:
    :return: True if pentagonal.
    """
    _, x = quadratic.solve(3, -1, -2 * n)
    return is_number(x) and x.is_integer()


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


def digits(x):
    """
    Returns the the digits of a number.
    Reference: https://en.wikipedia.org/wiki/Digit_sum
    :param x: The number to sum the digits of.
    :param b: The base of the number system.
    :return: Sum of the number x.
    """
    # upper_bound = int(math.log(x, 10))
    # reversed_digits = [1 / 10 ** n * (x % 10 ** (n + 1) - x % 10 ** n)
    #                    for n in range(upper_bound + 1)]
    # return list(map(int, reversed_digits))[::-1]
    return [int(d) for d in str(x)]


def digits_to_int(x):
    """
    Concatenate a list of digits to an integer.
    :param x:
    :return:
    """
    return int(''.join([str(i) for i in x]))


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
    if x < 2:
        raise ValueError('Function approximation is wrong when x < 2.')
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


def lcm(a, b):
    """
    Calculate the least common multiple (LCM) with the GCD
    algorithm using: LCM(a,b) = (a*b)/GCD(a,b).
    :param a:
    :param b:
    :return:
    """
    return a * b / gcd(a, b)


def lcm3(a, b, c):
    """
    Calculating the LCM for multiple digits is done with
    LCM(a,b,c) = LCM(LCM(a,b),c)
    :param a:
    :param b:
    :param c:
    :return:
    """
    return lcm(lcm(a, b), c)


def primitive_pythagorean_triplet_generator(n=math.inf):
    """
    Generates n primitive pythagorean triplets.
    :param n:
    :return:
    """
    v = 2
    u = 1
    while n > 0:
        if not(is_odd(v) and is_odd(u)) and gcd(u, v) == 1:
            a = v*v - u*u
            b = 2*v*u
            c = u*u + v*v
            n -= 1
            yield (a, b, c)
        u += 1
        if u >= v:
            v += 1
            u = 1


def prime_counting_function(n):
    """
    Return the number of primes below a given number.
    This is calculated with the proportionality which
    states that π(n) ~ n / log(n).
    :param n: Upper bound.
    :return: Estimate of the number of primes below the
             bound.
    """
    return n / math.log(n)


def lambertw(x):
    """
    Lambert W function with Newton's Method.
    :param x:
    :return:
    """
    eps = 1e-8
    w = x
    while True:
        ew = math.exp(w)
        w_new = w - (w * ew - x) / (w * ew + ew)
        if abs(w - w_new) <= eps:
            break
        w = w_new
    return w


def prime_counting_function_inv(y):
    """
    Returns the upper bound for a given number of primes.
    :param y: How many primes you want.
    :return: Upper bound.
    """
    x = 2
    while x / math.log(x) < y:
        x += 1
    return x


def product(numbers):
    """
    Returns the product of a list of numbers.
    :param numbers:
    :return:
    """
    p = 1
    for x in numbers:
        p *= x
    return p


def factorial(n):
    """
    Returns the factorial n! of a number.
    :param n:
    :return:
    """
    return n * factorial(n - 1) \
        if n > 0 \
        else 1


def is_even(n):
    """
    Returns true if a number is even.
    :param n:
    :return:
    """
    return n % 2 == 0


def is_odd(n):
    """
    Returns true if a number is odd.
    :param n:
    :return:
    """
    return n % 2 == 1


def permutations(a):
    """
    Generates all the permutations for a set.
    :param a:
    :return:
    """
    n = len(a)
    return _heap_perm_(n, a)


def _heap_perm_(n, a):
    """
    Heap's permutation algorithm.
    https://stackoverflow.com/a/29044942
    :param n:
    :param a:
    :return:
    """
    if n == 1: yield a
    else:
        for i in range(n-1):
            for hp in _heap_perm_(n-1, a): yield hp
            j = 0 if (n % 2) == 1 else i
            a[j], a[n - 1] = a[n - 1], a[j]
        for hp in _heap_perm_(n-1, a): yield hp


def shift(a, n=1):
    """
    Shift all the elements in the list by n.
    :param a:
    :param n:
    :return:
    """
    return a[n:] + a[:n]


def is_palindrome(x):
    """
    Returns true if a number or a string is a palindrome.
    :param x:
    :return:
    """
    chars = [c for c in x] if not is_number(x) else digits(x)
    for i in range(len(chars) // 2):
        if chars[i] != chars[len(chars) - i - 1]:
            return False
    return True


def is_pandigital_to_n(x, n, zero_based=False):
    return set(x) == set(range(0 if zero_based else 1, n + 1))


def to_binary_string(x):
    """
    Useful to convert a number into a binary number.
    :param x:
    :return:
    """
    return "{0:b}".format(x)


def _palindrome_number_generator():
    """
    https://stackoverflow.com/a/16344628
    :return:
    """
    yield 0
    lower = 1
    while True:
        higher = lower*10
        for i in range(lower, higher):
            s = str(i)
            yield int(s+s[-2::-1])
        for i in range(lower, higher):
            s = str(i)
            yield int(s+s[::-1])
        lower = higher


def palindromes(lower, upper):
    """
    Generates all palindromes between [lower, upper].
    https://stackoverflow.com/a/16344628
    :param lower:
    :param upper:
    :return:
    """
    all_palindrome_numbers = _palindrome_number_generator()
    for p in all_palindrome_numbers:
        if p >= lower:
            break
    palindrome_list = [p]
    for p in all_palindrome_numbers:
        # Because we use the same generator object,
        # p continues where the previous loop halted.
        if p >= upper:
            break
        palindrome_list.append(p)
    return palindrome_list


def string_split_2d(data, field_delimiter=',', line_delimiter='\n'):
    """
    Split a string of 2D data into lists. Example of the data
    1,2
    3,4
    5,6
    to:
    [[1,2],[3,4],[5,6]]
    :param data:
    :param field_delimiter: delimiter used between seperate fields, default: ,
    :param line_delimiter: delimiter used between lines, default: \n
    :return: 2D list
    """
    return [line.split(field_delimiter) for line in data.split(line_delimiter)]