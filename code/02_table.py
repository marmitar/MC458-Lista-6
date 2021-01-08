from typing import Sequence, Iterator


def imbalance(S: Sequence[int]) -> int:
    return max(S) - min(S)


def seq(k: int) -> Iterator[int]:
    while True:
        yield 1 if k & 1 else -1
        k = k >> 1


def constructions(P: Sequence[int], k: int=1) -> Iterator[tuple[int]]:
    for i in range(2 ** len(P)):
        yield tuple(p + s*k for p, s in zip(P, seq(i)))


if __name__ == "__main__":
    import sys
    # sys.argv = "X 12.33 2 1 3 1".split()

    k = float(sys.argv[-1])
    P = [int(a) for a in sys.argv[1:-1]]

    print(imbalance(P), k, len(P))
    for cr in constructions(P, k):
        print(cr, imbalance(cr))
