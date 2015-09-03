import math


def is_prime(x):
    for i in range(2, int(round(x ** 0.5) + 1)):
        if x % i == 0:
            return False
    return True


def main():
    bigger = [0, 0, 0]
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            count = 0
            n = 0
            while True:
                x = n**2 + a*n + b
                if is_prime(math.fabs(x)):
                    count += 1
                else:
                    break
                n += 1
            if count > bigger[0]:
                bigger = [count, a, b]
    return bigger, bigger[1]*bigger[2]

print(main())