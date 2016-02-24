#!/usr/bin/python
"""
https://www.codechef.com/problems/MAXDIFF

Testing:
    nosetests --with-doctest <file>

Example:

Input:
2
5 2
8 4 5 2 10
8 3
1 1 1 1 1 1 1 1

Output:
17
2
"""


def alg(k, w):
    """
    >>> alg(2, [8, 4, 5, 2, 10])
    17
    >>> alg(4, [8, 4, 5, 2, 10])
    25
    >>> alg(3, [1, 1, 1, 1, 1, 1, 1, 1])
    2
    """
    w = sorted(w)
    k2 = len(w) - k
    res1 = abs(sum(w[k:]) - sum(w[:k]))
    res2 = abs(sum(w[k2:]) - sum(w[:k2]))
    return max(res1, res2)


if __name__ == "__main__":

    for _ in range(input()):
        n, k = map(int, raw_input().split())
        w = map(int, raw_input().split())
        print alg(k, w)
