#!/usr/bin/python
"""
http://www.codechef.com/problems/CHEFLUCK

Testing:
    nosetests --with-doctest <file>

Input:
5
7
4
11
1
15

Output:
7
0
7
-1
7
"""


def alg(n):
    """
    >>> alg(7)
    7
    >>> alg(4)
    0
    >>> alg(11)
    7
    >>> alg(1)
    -1
    >>> alg(15)
    7
    """

    # my initial solution
    #while n % 7:
    #    n -= 4
    #if n < 0:
    #    return -1
    #return n

    # best solution
    d, m = divmod(n, 7)
    d -= m % 4
    return d * 7 if d >= 0 else -1


if __name__ == "__main__":

    for _ in range(input()):
        print alg(input())
