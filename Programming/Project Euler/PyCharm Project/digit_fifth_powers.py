def digit_fourth_powers():
    """
    a*10^4 + b*10^3 + c*10^2 + d = a^4 + b^4 + c^4 + d^4
    :return:
    """
    tuples = []
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    if a*10**4 + b*10**3 + c*10**2 + d == a**4 + b**4 + c**4 + d**4:
                        tuples.append(a**4 + b**4 + c**4 + d**4)
    for t in tuples:
        print(t)


digit_fourth_powers()