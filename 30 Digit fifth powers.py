wynik = 0
for a in range(2, 1000000):
    a = str(a)
    sum = 0
    for x in a:
        sum+=int(x)**5
    if sum == int(a):
       wynik += int(a)
print(wynik)