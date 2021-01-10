from typing import Sequence, Iterator


def imbalance(S: Sequence[int]) -> int:
    return max(S) - min(S)


def seq(k: int) -> Iterator[int]:
    while True:
        yield 1 if k & 1 else -1
        k = k >> 1


def constructions(P: Sequence[int], k: int=1) -> Iterator[tuple[int, ...]]:
    for i in range(2 ** len(P)):
        yield tuple(p + s*k for p, s in zip(P, seq(i)))

def show(C: tuple[int, ...]):
    print(','.join(f'{c:4d}' for c in C), '\t\t', imbalance(C))


def minimum(P: Sequence[int], k: int=1) -> tuple[int, ...]:
    return min(constructions(P, k), key=imbalance)


if __name__ == "__main__":
    import sys
    # sys.argv = "X 12.33 2 1 3 1".split()

    all = False
    if (k := sys.argv.pop()).startswith('-'):
        all = True
        k = sys.argv.pop()

    k = int(k)
    P = [int(a) for a in sys.argv[1:]]
    P.sort()

    if all:
        for cr in constructions(P, k):
            show(cr)

    print(imbalance(P), k, len(P))
    show(minimum(P, k))
