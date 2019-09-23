from math import sqrt


def is_invalid_polynomial(a, b):
    return a == 0 and b == 0


def is_first_degree_polynomial(a, b):
    return a == 0 and b != 0


def calculate_discriminant(a, b, c):
    return b * b - 4 * a * c


def first_degree_solution(b, c):
    return -c / b


def negative_solution(a, b, discriminant):
    return (-b - sqrt(discriminant)) / (2 * a)


def positive_solution(a, b, discriminant):
    return (-b + sqrt(discriminant)) / (2 * a)


def solve(a, b, c):
    """
    Solves a polynomial of the form: ax^2 + bx + c = 0.
    :param a: value of a in ax^2.
    :param b: value of b in bx.
    :param c: value of the constant c.
    :return: the solution as a tuple (s1, s2), where s2 is None
             if there is only a single solution.
    """
    if is_invalid_polynomial(a, b):
        raise ValueError('Invalid polynomial.')

    if is_first_degree_polynomial(a, b):
        return first_degree_solution(b, c), None

    discriminant = calculate_discriminant(a, b, c)

    if discriminant < 0:
        raise ValueError('Negative discriminant, there is no real solution.')

    if discriminant == 0:
        return positive_solution(a, b, discriminant), None

    return negative_solution(a, b, discriminant), positive_solution(a, b, discriminant)
