def incr(t: list[int]) -> bool:
    t[0] += 1

    for i in range(len(t) - 1):
        if t[i] > 1:
            t[i] = -1
            t[i + 1] += 1
        else:
            return True
    return t[len(t) - 1] <= 1


def num(t: list[int]) -> int:
    b = 1
    res = 0

    for ti in t:
        res += ti * b
        b *= 3
    return res

def show(t: list[int], neg: bool=False):
    n = num(t)
    if not neg and n < 0:
        return

    print(*(f'{i:2d}' for i in t), sep=',', end='')
    print('\t', f'{n:10d}')


def table(k: int, neg: bool=False):
    t = [-1] * (k + 1)

    show(t, neg)
    while incr(t):
        show(t, neg)


if __name__ == "__main__":
    import sys

    neg = len(sys.argv) > 2
    k = int(sys.argv[1])

    table(k, neg)
