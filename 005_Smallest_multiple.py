def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
def wynik(x):
    lcm=1
    for a in range(2,(x+1)):
        za=a*lcm/(gcd(a, lcm))
        lcm = za
    return lcm
print(wynik(20))
