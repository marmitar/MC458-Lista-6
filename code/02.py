from typing import Iterable, Iterator, TypeVar


def imbalance(S: list[int]) -> int:
    return S[-1] - S[0]


def min_imbalance(S: list[int], k: int) -> int:
    if len(S) == 1:
        return 0

    lim = S[0] + k, S[-1] - k
    inf, sup = min(lim), max(lim)

    for si in S[1:-1]:
        sub, add = si - k, si + k

        if sub < inf and add > sup:
            if sup - sub <= add - inf:
                inf = sub
            else:
                sup = add

    return min(sup - inf, S[-1] - S[0])


def min_imbalance_sk(S: list[int]) -> tuple[int, int]:
    if len(S) == 0:
        raise ValueError()

    min_k, min_diff = 0, imbalance(S)
    for k in range(1, imbalance(S)):
        diff = min_imbalance(S, k)
        if diff < min_diff:
            min_k, min_diff = k, diff
        elif diff > min_diff:
            break

    return min_k, min_diff

T = TypeVar('T')
def skip(it: Iterable[T], n: int=1) -> Iterator[T]:
    it = iter(it)
    for i in range(n):
        next(it)
    return it


def min_imbalance_gr(S: list[int]) -> tuple[int, list[int]]:
    if len(S) == 1:
        return 0

    inf, sup = min(S), max(S)

    ans = [None] * len(S)
    ans[0], ans[-1] = 1, -1
    lgu, sgd = S[0], S[-1]

    for i, si in skip(enumerate(S[:-1])):
        if sup - si > si - inf:
            ans[i] = 1
            if si > lgu:
                lgu = si
        else:
            ans[i] = -1
            if si < sgd:
                sgd = si

    k = min(sgd - inf, sup - lgu) // 2
    cfg = [si+k*d for si, d in zip(S, ans)]
    return k, cfg


if __name__ == "__main__":
    import sys, base64
    sys.argv = "X 4 1 8 10 20 13 721437".split()

    P = [int(a) for a in sys.argv[1:]]
    P.sort()
    print("D0 =", imbalance(P), "n =", len(P), "P = ", P)

    k1, D = min_imbalance_sk(P)
    print("k = ", k1, "Dk =", D)

    k2, cfg = min_imbalance_gr(P)
    print("k = ", k2, "Dk =", imbalance(cfg), "cfg =", cfg)

    if k1 != k2:
        args = ' '.join(sys.argv[1:])
        key = hash(args).to_bytes(8, 'little', signed=True)
        key = base64.b64encode(key)

        with open(f'{key}.txt', 'w') as file:
            print(args, file=file)

        print('ERROR!', f'{key}.txt', 'k1 =', k1, 'k2 =', k2)

