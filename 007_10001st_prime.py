def pier():
    lis=[]
    x=2
    while 1<2:
        cos=[]
        hi=0
        for a in range(2,x):
            hi=hi+1
        for a in range(2,x):
            if x%a == 0:
                break
            if x%a != 0:
                cos.append(a)
            if len(cos)==hi:
                lis.append(x)
            if len(lis) == 10001:
                wynik = lis[10000]
                return wynik
        x+=1
print(pier())