from typing import Sequence


def imbalance(S: Sequence[int]) -> int:
    return S[-1] - S[0]


def min_imbalance(S: Sequence[int], k: int) -> int:
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


def min_imbalance_sk(S: Sequence[int]) -> tuple[int, int]:
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


if __name__ == "__main__":
    import sys
    # sys.argv = "X 4 1 10".split()

    P = [int(a) for a in sys.argv[1:]]
    P.sort()
    print("D0 =", imbalance(P), "n =", len(P), "P = ", P)

    k, D = min_imbalance_sk(P)
    print("k = ", k, "Dk =", D)
