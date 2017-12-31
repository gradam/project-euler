__author__ = 'Kuba'
import itertools


def is_good(n):
    numbers = [2, 3, 5, 7, 11, 13, 17]
    for z, x in enumerate(range(1, 8)):
        if not int(n[x:x+3]) % numbers[z] == 0:
            return False
    return True

def main():
    suma = 0
    pandigits = itertools.permutations([str(x) for x in range(10)])
    for n in pandigits:
        n = ''.join(n)
        if is_good(n):
            suma += int(n)
    print(suma)


if __name__ == '__main__':
    main()
