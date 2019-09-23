import eulerlib


coins = [1, 2, 5, 10, 20, 50, 100, 200]
memo = {}


def coin_sums(t, c=7):
    if c <= 0 or t <= 0:
        return 1
    if (t, c) in memo.keys():
        return memo[(t, c)]
    res = sum([coin_sums(t - i * coins[c], c - 1) for i in range(t // coins[c] + 1)])
    memo[(t, c)] = res
    return res


eulerlib.time_it(coin_sums, [200])
