#!/usr/bin/python
"""
http://www.codechef.com/problems/ANUUND

Testing:
    nosetests --with-doctest <file>

Input:
2
2
3 2
3
10 5 2

Output:
2 3
2 10 5
"""


def alg(a):
    """
    >>> alg([3, 2])
    [2, 3]
    >>> alg([10, 5, 2])
    [2, 10, 5]
    >>> alg(range(5))
    [0, 4, 1, 3, 2]
    """
    a.sort()
    b = []
    for i in range(len(a)):
        # pop operations are memory inefficient
        if i % 2 == 0:
            b.append(a[i/2])
            # b.append(a.pop(0))
        else:
            b.append(a[-(i+1)/2])
            # b.append(a.pop())
    return b


if __name__ == "__main__":

    for t in range(input()):
        # we don't need N
        _ = input()

        a = map(int, raw_input().split())
        print " ".join(map(str, alg(a)))
