def ternary_dp(n: int) -> int:
    res = [-1] * (n + 1)
    res[0] = 0

    for i in range(1, n + 1):
        if i % 3 == 0:
            ans = res[i // 3]
        elif i % 3 == 1:
            ans = res[(i - 1) // 3]
        else:
            ans = res[(i + 1) // 3]

        res[i] = ans + 1

    return res[n] - 1


def ternary_gr(n: int) -> int:
    k = 0

    while n > 0:
        if n % 3 == 0:
            n = n // 3
        elif n % 3 == 1:
            n = (n - 1) // 3
        else:
            n = (n + 1) // 3

        k += 1
    return k - 1


if __name__ == "__main__":
    import sys

    n = int(sys.argv[1])
    k1 = ternary_dp(n)
    k2 = ternary_gr(n)

    print(k1, k2)
