from typing import overload


def bounds(t: list[int], M: float) -> range:
    lo = sum(ti * 2**i for i, ti in enumerate(t))
    return range(int(lo // M), sum(t))

def valid(t: list[int], s: list[int]) -> bool:
    for i in s:
        t[i] -= 1

    return not any(t)


@overload
def min_tiles_bf(t: list[int], M: float, keep: True) -> tuple[int, float, list[int]]: ...
@overload
def min_tiles_bf(t: list[int], M: float) -> tuple[int, list[int]]: ...
def min_tiles_bf(t: list[int], M: float, keep: bool=False) -> tuple[int, ...]:

    if sum(t) == 0:
        return 0, 0, []

    min, rem, cr = sum(t) + 1, None, None
    for i, ti in enumerate(t):
        if ti == 0:
            continue

        t[i] -= 1
        n, r, c = min_tiles_bf(t, M, True)
        t[i] = ti

        if r < 2**ti:
            n += 1
            r = M

        if n < min:
            min = n
            rem = r - 2**ti
            cr = [i] + c

    if keep:
        return min, rem, cr
    else:
        return min, cr


def clean(t: list[int]) -> list[int]:
    for i in reversed(range(len(t))):
        if t[i] > 0:
            return t[:i+1]
    return []


def min_tiles_gr(t: list[int], M: float) -> tuple[int, list[int]]:
    n = 0
    res = []

    while (t := clean(t)):
        rem = int(M)
        for i in reversed(range(len(t))):
            r = min(t[i], rem // 2**i)
            t[i] -= r
            rem -= r * 2**i
            res += [i] * r

        n += 1
    return n, res


if __name__ == "__main__":
    import sys
    # sys.argv = "X 12.33 2 1 3 1".split()

    M = float(sys.argv[1])
    t = [int(a) for a in sys.argv[2:]]
    assert M >= 2**(len(t) - 1)

    n, c = min_tiles_gr(t, M)
    print(n, c)
    print([2**i for i in c])

    assert n in bounds(t, M)
    assert valid(t, c)
