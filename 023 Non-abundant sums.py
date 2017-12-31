import math


def abu(x):
    abundant = []
    sumy = []
    wynik = 0
    liczby = [x for x in range(1, x + 1)]
    y=0
    for a in range(2, x + 1):
        wyn = []
        for i in range(2, round(math.sqrt(a)) + 1):
            if a % i == 0:
                wyn.append(i)
                if a / i != i:
                    wyn.append(a / i)
        if sum(wyn) + 1 > a:
            abundant.append(a)
    for a in abundant:
        for z in range(y, len(abundant)):
            sumy.append(a + abundant[z])
        y+=1
    wynik = sum(list(set(liczby) - set(sumy)))
    return wynik
print(abu(28123))
