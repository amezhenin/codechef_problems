#!/usr/bin/python
"""
http://www.codechef.com/problems/RRECIPE

Testing:
    nosetests --with-doctest <file>


Input:
5
?
??
ab?
a?c
aba

Output:
26
26
1
0
1
"""


def alg(s):
    """
    >>> alg('?')
    26
    >>> alg('??')
    26
    >>> alg('ab?')
    1
    >>> alg('a?c')
    0
    >>> alg('aba')
    1
    """

    res = 1
    for i in range((len(s)+1)/2):
        if s[i] == s[-i-1] == '?':
            res = res * 26 % 10000009
        elif s[i] != '?' and s[-i-1] != '?' and s[i] != s[-i-1]:
            return 0
    return res


if __name__ == "__main__":

    for _ in range(input()):
        print alg(raw_input())
