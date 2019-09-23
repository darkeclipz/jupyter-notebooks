import eulerlib


def fraction_to_decimal(numerator, denominator):
    """
    https://www.geeksforgeeks.org/find-recurring-sequence-fraction/
    :param numerator:
    :param denominator:
    :return:
    """
    result = str(int(numerator / denominator))
    list_of_previous_remainders = []
    remainder = numerator % denominator

    if remainder > 0:
        result += '.'

    while remainder != 0 and remainder not in list_of_previous_remainders:
        list_of_previous_remainders.append(remainder)
        remainder *= 10
        result += str(remainder // denominator)
        remainder = remainder % denominator

    cycle_length = len(list_of_previous_remainders) - list_of_previous_remainders.index(remainder) \
        if remainder in list_of_previous_remainders \
        else 0

    is_cyclic = remainder in list_of_previous_remainders

    return result, is_cyclic, cycle_length


def reciprocal_cycles():

    denominator_with_largest_cycle = 0
    largest_cycle = 0
    longest_decimal = ""

    for d in range(2, 1000):
        decimal, is_cyclic, cycle_length = fraction_to_decimal(1, d)
        if is_cyclic and cycle_length > largest_cycle:
            denominator_with_largest_cycle = d
            largest_cycle = cycle_length
            longest_decimal = decimal

    print('Denominator with largest cycle: {}'.format(denominator_with_largest_cycle))
    print('Cycle length: {}'.format(largest_cycle))
    print('Decimal as string: {}'.format(longest_decimal))
    print('Decimal as float: {}'.format(1 / denominator_with_largest_cycle))

    return denominator_with_largest_cycle


def reciprocal_cycles_primes():

    denominator_with_largest_cycle = 0
    largest_cycle = 0
    longest_decimal = ""
    primes = [i for i, v in enumerate(eulerlib.prime_sieve(1000)) if v]

    for d in primes:
        decimal, is_cyclic, cycle_length = fraction_to_decimal(1, d)
        if is_cyclic and cycle_length > largest_cycle:
            denominator_with_largest_cycle = d
            largest_cycle = cycle_length
            longest_decimal = decimal

    print('Denominator with largest cycle: {}'.format(denominator_with_largest_cycle))
    print('Cycle length: {}'.format(largest_cycle))
    print('Decimal as string: {}'.format(longest_decimal))
    print('Decimal as float: {}'.format(1 / denominator_with_largest_cycle))

    return denominator_with_largest_cycle


eulerlib.time_it(reciprocal_cycles)
eulerlib.time_it(reciprocal_cycles_primes)
