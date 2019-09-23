import eulerlib


def digit_powers(n):
    numbers = [i for i in range(2, 9**n*n + 1)
               if sum(map(lambda x: x**n, eulerlib.digits(i))) == i]
    print('Numbers found: {}'.format(numbers))
    return sum(numbers)


eulerlib.time_it(digit_powers, [5])
