#!/usr/bin/python
"""
http://www.codechef.com/problems/MAXCOUNT

Testing:
    nosetests --with-doctest <file>

Input:
2
5
1 2 3 2 5
6
1 2 2 1 1 2

Output:
2 2
1 3
"""

from collections import Counter

def read_n_array(fn=int):
    """
    Read array of integers with leading N. Optional param can change
    conversion to function to float.
    :return tuple (N, list)
    """
    n = input()
    a = raw_input()
    l = [fn(i) for i in a.split()]
    return n, l


def alg(a):
    """
    >>> alg([1, 2, 3, 2, 5])
    (2, 2)
    >>> alg([1, 2, 2, 1, 1, 2])
    (1, 3)
    >>> alg([100, 20, 20, 100, 100, 20, 20, 3, 3, 3, 3, 4, 4, 4, 4])
    (3, 4)
    """

    # My solution
    #res = Counter(a).most_common()
    #max_val = res[0][1]
    #candidats = filter(lambda x: x[1]==max_val, res)
    #return sorted(candidats)[0]

    # better solution by http://www.codechef.com/users/stelek
    res = Counter(a)
    return max(res.items(), key=lambda x: (x[1], -x[0]))


if __name__ == "__main__":
    for _ in range(input()):
        _, a = read_n_array()
        print "%s %s" % alg(a)
