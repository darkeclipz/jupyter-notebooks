import eulerlib


def triangular_pentagonal_hexagonal():
    i = 144
    hexagonal = eulerlib.hexagonal_number(i)
    while not (eulerlib.is_pentagonal_number(hexagonal) and eulerlib.is_triangle_number(hexagonal)):
        i += 1
        hexagonal = eulerlib.hexagonal_number(i)
    return hexagonal


eulerlib.time_it(triangular_pentagonal_hexagonal)
