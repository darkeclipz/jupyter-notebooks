import eulerlib


def digit_cancelling_fractions():
    lowest_nums = []
    lowest_denoms = []
    for den in range(10, 100):
        if den % 10 == 0:
            continue
        for num in range(10, den):
            num_digits = eulerlib.digits(num)
            den_digits = eulerlib.digits(den)
            if num % 10 == 0:
                continue
            digits_intersection = list(set(num_digits) & set(den_digits))
            if len(digits_intersection) > 0:
                num_digits.remove(digits_intersection[0])
                den_digits.remove(digits_intersection[0])
                num_lct = eulerlib.digits_to_int(num_digits)
                den_lct = eulerlib.digits_to_int(den_digits)
                cancelled_fraction = num_lct / den_lct
                fraction = num / den
                if fraction == cancelled_fraction:
                    lowest_nums.append(num_lct)
                    lowest_denoms.append(den_lct)
                    print('{} / {} = {} / {}'.format(num, den, num_lct, den_lct))

    num_prod = eulerlib.product(lowest_nums)
    den_prod = eulerlib.product(lowest_denoms)
    gcd = eulerlib.gcd(num_prod, den_prod)
    return den_prod / gcd


eulerlib.time_it(digit_cancelling_fractions)
