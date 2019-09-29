import eulerlib


def digit_factorials():
    result = 0
    factorials = [eulerlib.factorial(i) for i in range(10)]
    for n in range(4 * eulerlib.factorial(8) + 1):
        digits_of_n = [int(i) for i in str(n)]
        n_fact = sum([factorials[digit] for digit in digits_of_n])
        if n == n_fact:
            print(n)
            result += n_fact
    return result - 3


eulerlib.time_it(digit_factorials)
