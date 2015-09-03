import math


def cel(x):
    wyniki = []
    licz = []
    ind = 0
    il = []
    for a in range(1, x+1):
        wyn = []
        for y in range(1,round(math.sqrt(a))+1):
            if a%y==0:
                wyn.append(y)
                wyn.append(a/y)
        wyn = list(set(wyn))
        wyniki.append(sum(wyn)-a)
        licz.append(a)
    for a in wyniki:
        if a in licz:
            if licz[ind] == wyniki[int(a)-1]:
                if licz[ind] != licz[int(a)-1]:
                    if licz[ind] not in il:
                        il.append(licz[ind])
                        il.append(licz[int(a)-1])
        ind += 1
    return sum(il)
print(cel(10000))