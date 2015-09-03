import math


wynik = 0
for x in range(3,1000000):
    x = str(x)
    suma = 0
    for a in x:
        suma+=math.factorial(int(a))
    if suma == int(x):
        wynik+=int(x)
print(wynik)