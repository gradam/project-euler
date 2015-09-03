__author__ = 'Kuba'


def main():
    suma = 0
    for n in range(1000000):
        if str(n) == str(n)[::-1] and str(bin(n)).lstrip('0b') == str(bin(n))[::-1].rstrip('0b'):
            suma += n
    print(suma)


if __name__ == '__main__':
    main()