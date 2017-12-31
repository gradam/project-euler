__author__ = 'Kuba'
import math


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


def main():
    for n in range(10000):
        P1 = (3 * n**2 - n) / 2
        for n2 in range(10000):
            P2 = (3 * n**2 - n) / 2
            if is_penragonal(P1 - P2) and is_penragonal(P1 + P2):
                print('P1 = ' + str(P1) + '    P2 = ' + str(P2) + '   D = ' + str(abs(P2 - P1)))

if __name__ == '__main__':
    main()
