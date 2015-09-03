def is_prime(x):
    for i in range(2, int(round(x ** 0.5) + 1)):
        if x % i == 0:
            return False
    return True


def is_even(x):
    x = str(x)
    for i in x:
        if int(i) % 2 == 0 or int(i) == 5:
            return False
    return True


def is_circ(x):
    x = str(x)
    for i in range(len(x)):
        if not is_prime(int(x[i:] + x[:i])):
            return False
    return True


def num(x):
    ilosc = 2
    for i in range(2, x + 1):
        if is_even(i) and is_prime(i) and is_circ(i):
            ilosc += 1
    return ilosc


print(num(1000000))