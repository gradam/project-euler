def cos(x):
    x=x**1000
    x=str(x)
    wyn=0
    for a in x:
        wyn+=int(a)
    return wyn

print(cos(2))




print (sum([int(x) for x in str(2 ** 1000)]))

print(2**99999)