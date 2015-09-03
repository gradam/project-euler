__author__ = 'Kuba'

import pyprimes
import itertools


def is_truncatable(n):
    n2 = str(n)
    n1 = str(n)
    for _ in range(len(str(n))):
        if pyprimes.isprime(int(n1)) and pyprimes.isprime(int(n2)):
            n1 = n1[1::]
            n2 = n2[:-1:]
        else:
            return False
    return True




def main():
    suma = 0
    count = 0
    for n in itertools.count(10):
        if is_truncatable(n):
            suma += n
            count += 1
            if count == 11:
                print('SUMA: ' + str(suma))
                break


if __name__ == '__main__':
    main()