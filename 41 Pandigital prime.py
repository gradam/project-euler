def is_pandigital(x):
    y = str(x)
    cyfry = []
    for z in y:
        if z in cyfry or int(z) == 0:
            return False
        cyfry.append(z)
    numbers = "123456789"
    cyfry.sort()
    lenght = len(cyfry)
    if "".join(cyfry) == numbers[0:lenght]:
        return True
    return False


def is_prime(x):
    print(x)
    for z in range(3, int(x**0.5)+1, 2):
        if x % z == 0:
            return False
    return True


def main():
    for x in range(987654321, 1, -2):
        if is_pandigital(x):
            if is_prime(x):
                return x

print(main())