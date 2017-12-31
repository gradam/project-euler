def is_good(x):
    x = list(x)
    x.sort()
    if ''.join(x) == "123456789":
        return True
    return False


def main():
    wyn = []
    for x in range(10, 50):
        for a in range(100, 500):
            b = x * a
            if b > 9999:
                break
            if is_good(''.join([str(x), str(a), str(b)])):
                wyn.append(b)
    for x in range(1, 5):
        for a in range(1000, 2000):
            b = x * a
            if b > 9999:
                break
            if is_good(''.join([str(x), str(a), str(b)])):
                wyn.append(b)
    print(sum(set(wyn)))


main()