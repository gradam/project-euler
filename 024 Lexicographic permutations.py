import itertools

def lexi(x):
    wyniki = []
    for perm in itertools.permutations(range(10)):
        if len(wyniki) == x+1:
            break
        else:
            wyniki.append(perm)
    return wyniki[x-1]
print(lexi(1000000))