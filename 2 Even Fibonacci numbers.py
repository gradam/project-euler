def pt(kupa):
    ind1 = 0
    ind2 =1
    sum = 0
    licz = [1,2]
    wyn = 0
    while sum < kupa:
        licz.append(licz[ind1]+licz[ind2])
        sum = licz[len(licz)-1]
        ind1+=1
        ind2+=1
    for x in licz:
        if x%2==0:
            wyn = wyn+x
    return wyn
print(pt(4000000))