__author__ = 'Kuba'
import math, itertools


def is_penragonal(P):
    a = 3
    b = -1
    c = -1 * P * 2
    delta = (b**2) - (4*a*c)
    n1 = (-b + math.sqrt(delta)) / (2 * a)
    if int(n1) == n1:
        return True
    else:
        return False


def is_hexagonal(H):
    a = 2
    b = -1
    c = -H
    delta = (b**2) - (4*a*c)
    n1 = (-b + math.sqrt(delta)) / (2 * a)
    if int(n1) == n1:
        return True
    else:
        return False


def main():
    for x in itertools.count(286):
        T = (x**2 + x) / 2
        if is_penragonal(T) and is_hexagonal(T):
            print(T)
            quit(0)


if __name__ == '__main__':
    main()
