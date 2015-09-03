def pit(x):
    z=x//2
    for a in range(1,z):
        for b in range(1,z):
            for c in range(1,z):
                if a+b+c==x and (a**2)+(b**2)==c**2:
                    lst = [a, b, c]
                    return lst
print(pit(1000))