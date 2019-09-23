import unittest
import eulerlib


class CommonDivisorTests(unittest.TestCase):
    def test_divisors_0(self):
        d = eulerlib.divisors(0)
        assert d == []

    def test_divisors_1(self):
        d = eulerlib.divisors(1)
        assert d == [1], 'Divisors should be 1'

    def test_divisors_10(self):
        d = eulerlib.divisors(10)
        assert d == [1, 2, 5, 10], 'Divisors should be 1, 2, 5, 10'

    def test_divisors_neg10(self):
        d = eulerlib.divisors(-10)
        assert d == [1, 2, 5, 10], 'Divisors should be 1, 2, 5, 10'

    def test_divisors_17(self):
        d = eulerlib.divisors(17)
        assert d == [1, 17], 'Divisors should be 1 and 17.'

    def test_divisors_1001(self):
        d = eulerlib.divisors(1001)
        assert d == [1, 7, 11, 13, 77, 91, 143, 1001]

    def test_sum_of_proper_divisors_sieve(self):
        sieve = eulerlib.sum_of_proper_divisors_sieve(100)
        assert len(sieve) == 101
        assert sieve[12] == 16


class NumberTests(unittest.TestCase):
    def test_is_perfect_number_not_1(self):
        assert not eulerlib.is_perfect_number(1)

    def test_is_perfect_number_6(self):
        assert eulerlib.is_perfect_number(6)

    def test_is_perfect_number_28(self):
        assert eulerlib.is_perfect_number(28)

    def test_is_abundant_number_not_1(self):
        assert not eulerlib.is_abundant_number(1)

    def test_is_abundant_number_18(self):
        assert eulerlib.is_abundant_number(18)

    def test_is_deficient_number_1(self):
        assert eulerlib.is_deficient_number(1)

    def test_is_deficient_number_11(self):
        assert eulerlib.is_deficient_number(11)

    def test_prime_sieve_12345(self):
        assert eulerlib.prime_sieve(5) == [False, False, True, True, False, True]

    def test_prime_sieve_997(self):
        assert eulerlib.prime_sieve(1000)[997]

    def test_digits(self):
        assert eulerlib.digits(123) == [1, 2, 3]


class FibonacciNumberTests(unittest.TestCase):
    def test_is_fibonacci_number_1(self):
        assert eulerlib.is_fibonacci_number(1)

    def test_is_fibonacci_number_2(self):
        assert eulerlib.is_fibonacci_number(2)

    def test_is_fibonacci_number_not_4(self):
        assert not eulerlib.is_fibonacci_number(4)

    def test_is_fibonacci_number_21(self):
        assert eulerlib.is_fibonacci_number(21)

    def test_fibonacci_1(self):
        assert eulerlib.fibonacci_n(1) == 1

    def test_fibonacci_1_inv(self):
        assert eulerlib.fibonacci_n_inv(2) == 3

    def test_fibonacci_50(self):
        assert eulerlib.fibonacci_n(50) == 12586269025

    def test_fibonacci_50_inv(self):
        assert eulerlib.fibonacci_n_inv(12586269025) == 50


if __name__ == '__main__':
    unittest.main()
